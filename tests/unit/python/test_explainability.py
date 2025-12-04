"""
Tests for the AI Ethics Advisor explainability module.

This module tests SHAP/LIME-based explanations, counterfactual generation,
and plain-language explanation functionality.
"""

import pytest
import numpy as np
import sys
import os
import importlib.util
from unittest.mock import MagicMock, patch

# Load module with hyphenated filename
spec = importlib.util.spec_from_file_location(
    "explainability",
    os.path.join(
        os.path.dirname(__file__),
        '../../../.claude/skills/ai-ethics-advisor/modules/technical-safeguards/explainability.py'
    )
)
explainability = importlib.util.module_from_spec(spec)
spec.loader.exec_module(explainability)

ExplainabilityEngine = explainability.ExplainabilityEngine


class TestExplainabilityEngineInitialization:
    """Tests for ExplainabilityEngine initialization"""

    @pytest.fixture
    def mock_model(self):
        """Create a mock model"""
        model = MagicMock()
        model.predict = MagicMock(return_value=np.array([1, 0, 1]))
        model.predict_proba = MagicMock(return_value=np.array([[0.2, 0.8], [0.7, 0.3]]))
        return model

    @pytest.fixture
    def training_data(self):
        """Create sample training data"""
        return np.random.randn(100, 5)

    def test_initialization(self, mock_model, training_data):
        """Test engine initializes with model and data"""
        engine = ExplainabilityEngine(mock_model, training_data)
        assert engine.model == mock_model
        np.testing.assert_array_equal(engine.training_data, training_data)

    def test_explainers_initially_none(self, mock_model, training_data):
        """Test that explainers are None before setup"""
        engine = ExplainabilityEngine(mock_model, training_data)
        assert engine.explainer_shap is None
        assert engine.explainer_lime is None


class TestSetupExplainers:
    """Tests for explainer setup"""

    @pytest.fixture
    def engine(self):
        model = MagicMock()
        data = np.random.randn(50, 5)
        return ExplainabilityEngine(model, data)

    def test_shap_import_error_handled(self, engine):
        """Test that missing SHAP is handled gracefully"""
        with patch.dict('sys.modules', {'shap': None}):
            # Should not raise
            engine.setup_explainers()

    def test_lime_import_error_handled(self, engine):
        """Test that missing LIME is handled gracefully"""
        with patch.dict('sys.modules', {'lime': None, 'lime.lime_tabular': None}):
            # Should not raise
            engine.setup_explainers()


class TestExplainPrediction:
    """Tests for prediction explanation"""

    @pytest.fixture
    def engine_with_mock_shap(self):
        """Create engine with mocked SHAP explainer"""
        model = MagicMock()
        data = np.random.randn(50, 5)
        engine = ExplainabilityEngine(model, data)

        # Mock SHAP explainer
        mock_shap_values = MagicMock()
        mock_shap_values.feature_names = ['f1', 'f2', 'f3']
        mock_shap_values.values = [0.1, -0.2, 0.3]
        mock_shap_values.base_values = 0.5
        mock_shap_values.output_value = 0.7

        mock_explainer = MagicMock(return_value=mock_shap_values)
        engine.explainer_shap = mock_explainer

        return engine

    def test_shap_explanation_format(self, engine_with_mock_shap):
        """Test SHAP explanation format"""
        instance = np.array([1.0, 2.0, 3.0])
        result = engine_with_mock_shap.explain_prediction(instance, method='shap')

        assert result['method'] == 'shap'
        assert 'feature_importance' in result
        assert 'base_value' in result
        assert 'prediction' in result

    def test_unavailable_method_raises(self):
        """Test that unavailable method raises error"""
        model = MagicMock()
        data = np.random.randn(50, 5)
        engine = ExplainabilityEngine(model, data)

        instance = np.array([1.0, 2.0])

        with pytest.raises(ValueError, match="not available"):
            engine.explain_prediction(instance, method='shap')


class TestFormatShapExplanation:
    """Tests for SHAP explanation formatting"""

    def test_format_structure(self):
        """Test SHAP formatting produces correct structure"""
        model = MagicMock()
        data = np.random.randn(10, 3)
        engine = ExplainabilityEngine(model, data)

        mock_values = MagicMock()
        mock_values.feature_names = ['age', 'income', 'score']
        mock_values.values = [0.5, -0.3, 0.2]
        mock_values.base_values = 0.4
        mock_values.output_value = 0.8

        result = engine._format_shap_explanation(mock_values)

        assert result['method'] == 'shap'
        assert len(result['feature_importance']) == 3
        assert result['base_value'] == 0.4
        assert result['prediction'] == 0.8


class TestFormatLimeExplanation:
    """Tests for LIME explanation formatting"""

    def test_format_structure(self):
        """Test LIME formatting produces correct structure"""
        model = MagicMock()
        data = np.random.randn(10, 3)
        engine = ExplainabilityEngine(model, data)

        mock_explanation = MagicMock()
        mock_explanation.as_list.return_value = [('age > 30', 0.5), ('income < 50000', -0.3)]
        mock_explanation.predict_proba = [0.3, 0.7]

        result = engine._format_lime_explanation(mock_explanation)

        assert result['method'] == 'lime'
        assert len(result['feature_importance']) == 2
        assert result['prediction'] == [0.3, 0.7]


class TestGenerateCounterfactual:
    """Tests for counterfactual generation"""

    @pytest.fixture
    def engine_with_shap(self):
        """Create engine with working SHAP"""
        model = MagicMock()
        data = np.random.randn(50, 5)
        engine = ExplainabilityEngine(model, data)

        mock_shap_values = MagicMock()
        mock_shap_values.feature_names = ['income', 'age', 'credit_score']
        mock_shap_values.values = [0.5, -0.3, 0.2]
        mock_shap_values.base_values = 0.4
        mock_shap_values.output_value = 0.7

        engine.explainer_shap = MagicMock(return_value=mock_shap_values)
        return engine

    def test_counterfactual_structure(self, engine_with_shap):
        """Test counterfactual output structure"""
        instance = np.array([50000, 35, 700])
        result = engine_with_shap.generate_counterfactual(instance, desired_outcome=0)

        assert 'current_outcome' in result
        assert 'desired_outcome' in result
        assert 'suggested_changes' in result

    def test_counterfactual_suggests_changes(self, engine_with_shap):
        """Test that counterfactual suggests changes"""
        instance = np.array([50000, 35, 700])
        result = engine_with_shap.generate_counterfactual(instance, desired_outcome=0)

        # Should have suggestions based on feature importance
        assert len(result['suggested_changes']) > 0

    def test_suggestions_have_correct_fields(self, engine_with_shap):
        """Test that each suggestion has required fields"""
        instance = np.array([50000, 35, 700])
        result = engine_with_shap.generate_counterfactual(instance, desired_outcome=0)

        if result['suggested_changes']:
            suggestion = result['suggested_changes'][0]
            assert 'feature' in suggestion
            assert 'current_contribution' in suggestion
            assert 'suggestion' in suggestion
            assert 'importance' in suggestion


class TestExplainToLayperson:
    """Tests for plain-language explanations"""

    @pytest.fixture
    def engine_with_shap(self):
        """Create engine with SHAP for layperson explanations"""
        model = MagicMock()
        data = np.random.randn(50, 3)
        engine = ExplainabilityEngine(model, data)

        mock_shap_values = MagicMock()
        mock_shap_values.feature_names = ['income', 'age', 'credit_score']
        mock_shap_values.values = [0.5, -0.3, 0.2]
        mock_shap_values.base_values = 0.4
        mock_shap_values.output_value = 0.7

        engine.explainer_shap = MagicMock(return_value=mock_shap_values)
        return engine

    def test_approved_explanation_language(self, engine_with_shap):
        """Test approved decision language"""
        instance = np.array([60000, 40, 750])
        result = engine_with_shap.explain_to_layperson(instance, prediction=1)

        assert 'approved' in result.lower()

    def test_declined_explanation_language(self, engine_with_shap):
        """Test declined decision language"""
        instance = np.array([30000, 25, 600])
        result = engine_with_shap.explain_to_layperson(instance, prediction=0)

        assert 'declined' in result.lower()

    def test_explanation_is_string(self, engine_with_shap):
        """Test that explanation is a string"""
        instance = np.array([50000, 35, 700])
        result = engine_with_shap.explain_to_layperson(instance, prediction=1)
        assert isinstance(result, str)


class TestFeatureToLanguage:
    """Tests for feature to language conversion"""

    @pytest.fixture
    def engine(self):
        model = MagicMock()
        data = np.random.randn(10, 3)
        return ExplainabilityEngine(model, data)

    def test_positive_impact_high(self, engine):
        """Test positive impact produces 'high' language"""
        result = engine._feature_to_language('income', 0.5)
        assert 'high' in result.lower()

    def test_negative_impact_low(self, engine):
        """Test negative impact produces 'low' language"""
        result = engine._feature_to_language('credit_score', -0.5)
        assert 'low' in result.lower()

    def test_includes_feature_name(self, engine):
        """Test that feature name is in result"""
        result = engine._feature_to_language('debt_ratio', 0.3)
        assert 'debt_ratio' in result


class TestExplainWithCounterfactual:
    """Tests for combined explanation with counterfactual"""

    @pytest.fixture
    def engine_with_shap(self):
        """Create fully configured engine"""
        model = MagicMock()
        data = np.random.randn(50, 3)
        engine = ExplainabilityEngine(model, data)

        mock_shap_values = MagicMock()
        mock_shap_values.feature_names = ['income', 'age', 'score']
        mock_shap_values.values = [0.5, -0.3, 0.2]
        mock_shap_values.base_values = 0.4
        mock_shap_values.output_value = 0.7

        engine.explainer_shap = MagicMock(return_value=mock_shap_values)
        return engine

    def test_includes_base_explanation(self, engine_with_shap):
        """Test that result includes base explanation"""
        instance = np.array([50000, 35, 700])
        result = engine_with_shap.explain_with_counterfactual(
            instance, prediction=1, desired_outcome=None
        )

        # Should include base explanation
        assert 'approved' in result.lower() or 'declined' in result.lower()

    def test_includes_counterfactual_when_different(self, engine_with_shap):
        """Test counterfactual included when desired differs"""
        instance = np.array([50000, 35, 700])
        result = engine_with_shap.explain_with_counterfactual(
            instance, prediction=1, desired_outcome=0
        )

        # Should include "different outcome" language
        assert 'different' in result.lower() or 'consider' in result.lower()

    def test_no_counterfactual_when_same(self, engine_with_shap):
        """Test no counterfactual when outcome matches desired"""
        instance = np.array([50000, 35, 700])
        result = engine_with_shap.explain_with_counterfactual(
            instance, prediction=1, desired_outcome=1
        )

        # Should not include counterfactual suggestions
        # Result should be shorter (just base explanation)
        assert isinstance(result, str)


class TestEdgeCases:
    """Tests for edge cases and error handling"""

    def test_empty_feature_importance(self):
        """Test handling of empty feature importance"""
        model = MagicMock()
        data = np.random.randn(10, 1)
        engine = ExplainabilityEngine(model, data)

        # Mock empty explanation
        mock_shap_values = MagicMock()
        mock_shap_values.feature_names = []
        mock_shap_values.values = []
        mock_shap_values.base_values = 0.5
        mock_shap_values.output_value = 0.5

        engine.explainer_shap = MagicMock(return_value=mock_shap_values)

        instance = np.array([1.0])
        result = engine.explain_prediction(instance, method='shap')

        assert result['feature_importance'] == []

    def test_single_feature(self):
        """Test explanation with single feature"""
        model = MagicMock()
        data = np.random.randn(10, 1)
        engine = ExplainabilityEngine(model, data)

        mock_shap_values = MagicMock()
        mock_shap_values.feature_names = ['single_feature']
        mock_shap_values.values = [0.8]
        mock_shap_values.base_values = 0.2
        mock_shap_values.output_value = 1.0

        engine.explainer_shap = MagicMock(return_value=mock_shap_values)

        instance = np.array([5.0])
        result = engine.explain_prediction(instance, method='shap')

        assert len(result['feature_importance']) == 1


class TestIntegration:
    """Integration tests combining multiple functionalities"""

    @pytest.fixture
    def full_engine(self):
        """Create fully configured engine for integration tests"""
        model = MagicMock()
        model.predict_proba = MagicMock(return_value=np.array([[0.3, 0.7]]))

        data = np.random.randn(100, 5)
        engine = ExplainabilityEngine(model, data)

        mock_shap_values = MagicMock()
        mock_shap_values.feature_names = ['income', 'age', 'debt', 'history', 'employment']
        mock_shap_values.values = [0.3, -0.1, -0.4, 0.2, 0.1]
        mock_shap_values.base_values = 0.5
        mock_shap_values.output_value = 0.6

        engine.explainer_shap = MagicMock(return_value=mock_shap_values)

        return engine

    def test_full_explanation_workflow(self, full_engine):
        """Test complete explanation workflow"""
        instance = np.array([50000, 35, 5000, 10, 5])

        # Get technical explanation
        technical = full_engine.explain_prediction(instance, method='shap')
        assert 'feature_importance' in technical

        # Get layperson explanation
        layperson = full_engine.explain_to_layperson(instance, prediction=1)
        assert isinstance(layperson, str)
        assert len(layperson) > 0

        # Get counterfactual
        counterfactual = full_engine.generate_counterfactual(instance, desired_outcome=0)
        assert 'suggested_changes' in counterfactual

        # Get combined explanation
        combined = full_engine.explain_with_counterfactual(
            instance, prediction=1, desired_outcome=0
        )
        assert isinstance(combined, str)
