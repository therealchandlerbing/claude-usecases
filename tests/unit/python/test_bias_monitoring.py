"""
Tests for the AI Ethics Advisor bias monitoring module.

This module tests fairness metrics calculation, threshold detection,
and bias monitoring functionality.
"""

import pytest
import numpy as np
import sys
import os

# Add module to path
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '../../../.claude/skills/ai-ethics-advisor/modules/technical-safeguards'
))

# Direct import now that files use underscores
from bias_monitoring import BiasMonitor, FairnessMetrics


class TestFairnessMetrics:
    """Tests for FairnessMetrics dataclass"""

    def test_fairness_metrics_creation(self):
        """Test that FairnessMetrics can be created"""
        metrics = FairnessMetrics(
            statistical_parity_difference=0.05,
            equalized_odds_difference=0.08,
            equal_opportunity_difference=0.03,
            predictive_parity_difference=0.04,
            disparate_impact_ratio=0.92
        )
        assert metrics.statistical_parity_difference == 0.05
        assert metrics.equalized_odds_difference == 0.08
        assert metrics.equal_opportunity_difference == 0.03
        assert metrics.predictive_parity_difference == 0.04
        assert metrics.disparate_impact_ratio == 0.92


class TestBiasMonitorInitialization:
    """Tests for BiasMonitor initialization"""

    def test_default_thresholds(self):
        """Test default fairness thresholds"""
        monitor = BiasMonitor(protected_attributes=['gender', 'race'])
        assert monitor.thresholds['statistical_parity'] == 0.1
        assert monitor.thresholds['equalized_odds'] == 0.1
        assert monitor.thresholds['equal_opportunity'] == 0.1
        assert monitor.thresholds['disparate_impact'] == 0.8

    def test_custom_thresholds(self):
        """Test custom fairness thresholds"""
        custom_thresholds = {
            'statistical_parity': 0.05,
            'equalized_odds': 0.05,
            'equal_opportunity': 0.05,
            'disparate_impact': 0.9
        }
        monitor = BiasMonitor(
            protected_attributes=['gender'],
            fairness_thresholds=custom_thresholds
        )
        assert monitor.thresholds['statistical_parity'] == 0.05
        assert monitor.thresholds['disparate_impact'] == 0.9

    def test_protected_attributes_stored(self):
        """Test that protected attributes are stored"""
        attrs = ['gender', 'race', 'age']
        monitor = BiasMonitor(protected_attributes=attrs)
        assert monitor.protected_attributes == attrs

    def test_violation_log_initialized(self):
        """Test that violation log is initialized empty"""
        monitor = BiasMonitor(protected_attributes=['gender'])
        assert monitor.violation_log == []


class TestStatisticalParityDifference:
    """Tests for statistical parity difference calculation"""

    @pytest.fixture
    def monitor(self):
        return BiasMonitor(protected_attributes=['gender'])

    def test_equal_rates(self, monitor):
        """Test SPD is 0 when rates are equal"""
        pred_a = np.array([1, 0, 1, 0, 1])
        pred_b = np.array([1, 0, 1, 0, 1])
        spd = monitor._statistical_parity_diff(pred_a, pred_b)
        assert spd == 0.0

    def test_group_a_higher_rate(self, monitor):
        """Test positive SPD when group A has higher positive rate"""
        pred_a = np.array([1, 1, 1, 1])  # 100% positive
        pred_b = np.array([1, 0, 0, 0])  # 25% positive
        spd = monitor._statistical_parity_diff(pred_a, pred_b)
        assert spd == 0.75

    def test_group_b_higher_rate(self, monitor):
        """Test negative SPD when group B has higher positive rate"""
        pred_a = np.array([0, 0, 1, 0])  # 25% positive
        pred_b = np.array([1, 1, 1, 1])  # 100% positive
        spd = monitor._statistical_parity_diff(pred_a, pred_b)
        assert spd == -0.75


class TestEqualizedOddsDifference:
    """Tests for equalized odds difference calculation"""

    @pytest.fixture
    def monitor(self):
        return BiasMonitor(protected_attributes=['gender'])

    def test_equal_tpr_and_fpr(self, monitor):
        """Test EOD is 0 when TPR and FPR are equal between groups"""
        pred_a = np.array([1, 1, 0, 0])
        actual_a = np.array([1, 1, 0, 0])
        pred_b = np.array([1, 1, 0, 0])
        actual_b = np.array([1, 1, 0, 0])

        eod = monitor._equalized_odds_diff(pred_a, actual_a, pred_b, actual_b)
        assert eod == 0.0

    def test_different_tpr(self, monitor):
        """Test EOD captures TPR differences"""
        pred_a = np.array([1, 1])  # TPR = 1.0
        actual_a = np.array([1, 1])
        pred_b = np.array([0, 0])  # TPR = 0.0
        actual_b = np.array([1, 1])

        eod = monitor._equalized_odds_diff(pred_a, actual_a, pred_b, actual_b)
        assert eod == 1.0

    def test_handles_empty_positive_class(self, monitor):
        """Test EOD handles case with no positive actuals"""
        pred_a = np.array([0, 0])
        actual_a = np.array([0, 0])  # No positives
        pred_b = np.array([1, 0])
        actual_b = np.array([0, 0])

        # Should not raise
        eod = monitor._equalized_odds_diff(pred_a, actual_a, pred_b, actual_b)
        assert isinstance(eod, float)


class TestEqualOpportunityDifference:
    """Tests for equal opportunity difference calculation"""

    @pytest.fixture
    def monitor(self):
        return BiasMonitor(protected_attributes=['gender'])

    def test_equal_tpr(self, monitor):
        """Test EOPD is 0 when TPR is equal"""
        pred_a = np.array([1, 1])
        actual_a = np.array([1, 1])
        pred_b = np.array([1, 1])
        actual_b = np.array([1, 1])

        eopd = monitor._equal_opportunity_diff(pred_a, actual_a, pred_b, actual_b)
        assert eopd == 0.0

    def test_tpr_difference(self, monitor):
        """Test EOPD captures TPR difference"""
        pred_a = np.array([1, 1, 0, 0])
        actual_a = np.array([1, 1, 1, 1])  # TPR = 0.5
        pred_b = np.array([1, 1, 1, 1])
        actual_b = np.array([1, 1, 1, 1])  # TPR = 1.0

        eopd = monitor._equal_opportunity_diff(pred_a, actual_a, pred_b, actual_b)
        assert eopd == 0.5


class TestPredictiveParityDifference:
    """Tests for predictive parity difference calculation"""

    @pytest.fixture
    def monitor(self):
        return BiasMonitor(protected_attributes=['gender'])

    def test_equal_precision(self, monitor):
        """Test PPD is 0 when precision is equal"""
        pred_a = np.array([1, 1, 0, 0])
        actual_a = np.array([1, 1, 0, 0])  # Precision = 1.0
        pred_b = np.array([1, 1, 0, 0])
        actual_b = np.array([1, 1, 0, 0])  # Precision = 1.0

        ppd = monitor._predictive_parity_diff(pred_a, actual_a, pred_b, actual_b)
        assert ppd == 0.0

    def test_precision_difference(self, monitor):
        """Test PPD captures precision difference"""
        pred_a = np.array([1, 1])
        actual_a = np.array([1, 1])  # Precision = 1.0
        pred_b = np.array([1, 1])
        actual_b = np.array([1, 0])  # Precision = 0.5

        ppd = monitor._predictive_parity_diff(pred_a, actual_a, pred_b, actual_b)
        assert ppd == 0.5


class TestDisparateImpactRatio:
    """Tests for disparate impact ratio calculation"""

    @pytest.fixture
    def monitor(self):
        return BiasMonitor(protected_attributes=['gender'])

    def test_equal_rates_returns_one(self, monitor):
        """Test DIR is 1.0 when rates are equal"""
        pred_a = np.array([1, 0, 1, 0])
        pred_b = np.array([1, 0, 1, 0])

        di = monitor._disparate_impact_ratio(pred_a, pred_b)
        assert di == 1.0

    def test_four_fifths_rule(self, monitor):
        """Test DIR below 0.8 indicates potential bias (four-fifths rule)"""
        pred_a = np.array([1, 1, 1, 1, 1, 1, 1, 1])  # 100% positive
        pred_b = np.array([1, 1, 1, 0, 0, 0, 0, 0])  # 37.5% positive

        di = monitor._disparate_impact_ratio(pred_a, pred_b)
        assert di < 0.8  # Violates four-fifths rule

    def test_handles_zero_rates(self, monitor):
        """Test DIR handles zero positive rates"""
        pred_a = np.array([0, 0, 0, 0])
        pred_b = np.array([0, 0, 0, 0])

        di = monitor._disparate_impact_ratio(pred_a, pred_b)
        assert di == 1.0  # Both rates are 0, ratio is defined as 1


class TestEvaluateFairness:
    """Tests for the main evaluate_fairness method"""

    @pytest.fixture
    def monitor(self):
        return BiasMonitor(
            protected_attributes=['gender', 'race'],
            fairness_thresholds={
                'statistical_parity': 0.1,
                'equalized_odds': 0.1,
                'equal_opportunity': 0.1,
                'disparate_impact': 0.8
            }
        )

    @pytest.fixture
    def fair_dataset(self):
        """Create a fair dataset"""
        np.random.seed(42)
        n = 100

        predictions = np.random.randint(0, 2, n)
        actuals = predictions.copy()  # Perfect predictions
        demographics = {
            'gender': np.array(['M', 'F'] * (n // 2)),
            'race': np.array(['A', 'B'] * (n // 2))
        }

        return predictions, actuals, demographics

    @pytest.fixture
    def biased_dataset(self):
        """Create a biased dataset"""
        n = 100

        # Group A gets more positive predictions
        gender = np.array(['M'] * 50 + ['F'] * 50)
        predictions = np.array([1] * 40 + [0] * 10 + [1] * 10 + [0] * 40)
        actuals = np.array([1] * 30 + [0] * 20 + [1] * 30 + [0] * 20)

        demographics = {'gender': gender}

        return predictions, actuals, demographics

    def test_returns_results_for_all_attributes(self, monitor, fair_dataset):
        """Test that results are returned for all protected attributes"""
        predictions, actuals, demographics = fair_dataset
        results = monitor.evaluate_fairness(predictions, actuals, demographics)

        assert 'gender' in results
        assert 'race' in results

    def test_returns_fairness_metrics(self, monitor, fair_dataset):
        """Test that FairnessMetrics are returned for each group pair"""
        predictions, actuals, demographics = fair_dataset
        results = monitor.evaluate_fairness(predictions, actuals, demographics)

        # Check that metrics exist for gender groups
        assert len(results['gender']) > 0

    def test_detects_bias(self, monitor, biased_dataset):
        """Test that bias is detected in biased dataset"""
        predictions, actuals, demographics = biased_dataset

        # Create monitor with single attribute
        single_monitor = BiasMonitor(
            protected_attributes=['gender'],
            fairness_thresholds={'statistical_parity': 0.1, 'disparate_impact': 0.8}
        )

        results = single_monitor.evaluate_fairness(predictions, actuals, demographics)

        # Should detect significant difference
        gender_metrics = results['gender']
        for groups, metrics in gender_metrics.items():
            # The biased dataset should show high SPD
            assert abs(metrics.statistical_parity_difference) > 0

    def test_skips_single_value_attributes(self, monitor):
        """Test that attributes with single value are skipped"""
        predictions = np.array([1, 0, 1, 0])
        actuals = np.array([1, 0, 1, 0])
        demographics = {
            'gender': np.array(['M', 'M', 'M', 'M']),  # Single value
            'race': np.array(['A', 'B', 'A', 'B'])
        }

        results = monitor.evaluate_fairness(predictions, actuals, demographics)

        # Gender should not be in results (only one unique value)
        assert 'gender' not in results or len(results.get('gender', {})) == 0


class TestViolationFlagging:
    """Tests for violation detection and logging"""

    @pytest.fixture
    def monitor(self):
        return BiasMonitor(
            protected_attributes=['gender'],
            fairness_thresholds={
                'statistical_parity': 0.1,
                'disparate_impact': 0.8,
                'equalized_odds': 0.1,
                'equal_opportunity': 0.1
            }
        )

    def test_flags_statistical_parity_violation(self, monitor):
        """Test that SPD violations are flagged"""
        results = {
            'gender': {
                ('M', 'F'): FairnessMetrics(
                    statistical_parity_difference=0.3,  # Above threshold
                    equalized_odds_difference=0.05,
                    equal_opportunity_difference=0.05,
                    predictive_parity_difference=0.05,
                    disparate_impact_ratio=0.9
                )
            }
        }

        violations = monitor._flag_violations(results)

        assert len(violations) > 0
        assert any(v['metric'] == 'statistical_parity' for v in violations)

    def test_flags_disparate_impact_violation(self, monitor):
        """Test that DI violations are flagged"""
        results = {
            'gender': {
                ('M', 'F'): FairnessMetrics(
                    statistical_parity_difference=0.05,
                    equalized_odds_difference=0.05,
                    equal_opportunity_difference=0.05,
                    predictive_parity_difference=0.05,
                    disparate_impact_ratio=0.6  # Below threshold
                )
            }
        }

        violations = monitor._flag_violations(results)

        assert len(violations) > 0
        assert any(v['metric'] == 'disparate_impact' for v in violations)

    def test_no_violations_for_fair_metrics(self, monitor):
        """Test that fair metrics don't trigger violations"""
        results = {
            'gender': {
                ('M', 'F'): FairnessMetrics(
                    statistical_parity_difference=0.05,
                    equalized_odds_difference=0.05,
                    equal_opportunity_difference=0.05,
                    predictive_parity_difference=0.05,
                    disparate_impact_ratio=0.9
                )
            }
        }

        violations = monitor._flag_violations(results)
        assert len(violations) == 0


class TestViolationLogging:
    """Tests for violation logging functionality"""

    def test_violations_logged_on_evaluate(self):
        """Test that violations are logged when evaluating"""
        monitor = BiasMonitor(
            protected_attributes=['gender'],
            fairness_thresholds={'statistical_parity': 0.01, 'disparate_impact': 0.99}
        )

        # Create biased dataset
        predictions = np.array([1, 1, 1, 1, 0, 0, 0, 0])
        actuals = np.array([1, 1, 1, 1, 0, 0, 0, 0])
        demographics = {'gender': np.array(['M', 'M', 'M', 'M', 'F', 'F', 'F', 'F'])}

        # Evaluate - should log violations
        monitor.evaluate_fairness(predictions, actuals, demographics)

        assert len(monitor.violation_log) > 0
        assert 'violations' in monitor.violation_log[0]
        assert 'timestamp' in monitor.violation_log[0]


class TestEdgeCases:
    """Tests for edge cases and boundary conditions"""

    @pytest.fixture
    def monitor(self):
        return BiasMonitor(protected_attributes=['gender'])

    def test_empty_arrays(self, monitor):
        """Test handling of empty arrays"""
        pred_a = np.array([])
        pred_b = np.array([])

        # Should handle gracefully (may return nan or 0)
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            with np.errstate(invalid='ignore', divide='ignore'):
                spd = monitor._statistical_parity_diff(pred_a, pred_b)
                # Empty arrays produce nan
                assert np.isnan(spd) or spd == 0

    def test_single_element_arrays(self, monitor):
        """Test handling of single element arrays"""
        pred_a = np.array([1])
        pred_b = np.array([0])

        spd = monitor._statistical_parity_diff(pred_a, pred_b)
        assert spd == 1.0  # 1.0 - 0.0

    def test_all_positive_predictions(self, monitor):
        """Test with all positive predictions"""
        pred_a = np.array([1, 1, 1, 1])
        pred_b = np.array([1, 1, 1, 1])

        di = monitor._disparate_impact_ratio(pred_a, pred_b)
        assert di == 1.0

    def test_all_negative_predictions(self, monitor):
        """Test with all negative predictions"""
        pred_a = np.array([0, 0, 0, 0])
        pred_b = np.array([0, 0, 0, 0])

        di = monitor._disparate_impact_ratio(pred_a, pred_b)
        assert di == 1.0  # Both 0, defined as 1
