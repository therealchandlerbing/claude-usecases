"""
Explainability tools for responsible AI

Provides methods for generating explanations of AI model decisions
using SHAP, LIME, and other interpretability techniques.
"""

import numpy as np
from typing import Dict, List


class ExplainabilityEngine:
    """
    Generate explanations for AI model decisions

    Usage:
        engine = ExplainabilityEngine(model, training_data)
        engine.setup_explainers()

        # Individual explanation
        explanation = engine.explain_prediction(instance, method='shap')

        # Plain language explanation
        text = engine.explain_to_layperson(instance, prediction)
    """

    def __init__(self, model, training_data):
        self.model = model
        self.training_data = training_data
        self.explainer_shap = None
        self.explainer_lime = None

    def setup_explainers(self):
        """Initialize explanation methods"""
        try:
            import shap
            # SHAP for global and local explanations
            self.explainer_shap = shap.Explainer(
                self.model,
                self.training_data
            )
        except ImportError:
            print("SHAP not available. Install with: pip install shap")

        try:
            import lime
            import lime.lime_tabular
            # LIME for local explanations
            self.explainer_lime = lime.lime_tabular.LimeTabularExplainer(
                self.training_data,
                mode='classification',
                feature_names=self.training_data.columns if hasattr(
                    self.training_data, 'columns'
                ) else None
            )
        except ImportError:
            print("LIME not available. Install with: pip install lime")

    def explain_prediction(
        self,
        instance: np.ndarray,
        method: str = 'shap'
    ) -> Dict:
        """
        Generate explanation for a single prediction

        Args:
            instance: Input instance to explain
            method: 'shap' or 'lime'

        Returns:
            Dictionary containing explanation details
        """
        if method == 'shap' and self.explainer_shap:
            shap_values = self.explainer_shap(instance)
            return self._format_shap_explanation(shap_values)
        elif method == 'lime' and self.explainer_lime:
            explanation = self.explainer_lime.explain_instance(
                instance,
                self.model.predict_proba
            )
            return self._format_lime_explanation(explanation)
        else:
            raise ValueError(f"Method {method} not available or not set up")

    def _format_shap_explanation(self, shap_values) -> Dict:
        """Format SHAP explanation for output"""
        return {
            'method': 'shap',
            'feature_importance': list(zip(
                shap_values.feature_names,
                shap_values.values
            )),
            'base_value': shap_values.base_values,
            'prediction': shap_values.output_value
        }

    def _format_lime_explanation(self, lime_explanation) -> Dict:
        """Format LIME explanation for output"""
        return {
            'method': 'lime',
            'feature_importance': lime_explanation.as_list(),
            'prediction': lime_explanation.predict_proba
        }

    def generate_counterfactual(
        self,
        instance: np.ndarray,
        desired_outcome: int
    ) -> Dict:
        """
        Generate counterfactual explanation:
        "What would need to change for a different outcome?"

        Args:
            instance: Current instance
            desired_outcome: Target outcome (0 or 1)

        Returns:
            Dictionary with suggested changes
        """
        # This is a simplified implementation
        # For production, use libraries like DiCE or Alibi

        # Get feature importance
        explanation = self.explain_prediction(instance, method='shap')
        feature_importance = explanation['feature_importance']

        # Identify most influential features
        top_features = sorted(
            feature_importance,
            key=lambda x: abs(x[1]),
            reverse=True
        )[:5]

        suggestions = []
        for feature, impact in top_features:
            # Suggest change direction based on impact and desired outcome
            if (impact > 0 and desired_outcome == 0) or \
               (impact < 0 and desired_outcome == 1):
                suggestions.append({
                    'feature': feature,
                    'current_contribution': impact,
                    'suggestion': f'Reduce {feature}' if impact > 0 else f'Increase {feature}',
                    'importance': abs(impact)
                })

        return {
            'current_outcome': 1 - desired_outcome,
            'desired_outcome': desired_outcome,
            'suggested_changes': suggestions
        }

    def explain_to_layperson(
        self,
        instance: np.ndarray,
        prediction: int,
        feature_names: List[str] = None
    ) -> str:
        """
        Generate plain-language explanation

        Args:
            instance: Input instance
            prediction: Model prediction (0 or 1)
            feature_names: Optional feature names for clarity

        Returns:
            Plain language explanation string
        """
        explanation = self.explain_prediction(instance)

        # Get top 3 factors
        top_factors = sorted(
            explanation['feature_importance'],
            key=lambda x: abs(x[1]),
            reverse=True
        )[:3]

        if prediction == 1:
            language = "This decision was approved primarily because "
        else:
            language = "This decision was declined primarily because "

        reasons = []
        for feature, impact in top_factors:
            readable_feature = self._feature_to_language(
                feature, impact, feature_names
            )
            reasons.append(readable_feature)

        language += ", ".join(reasons) + "."

        return language

    def _feature_to_language(
        self,
        feature: str,
        impact: float,
        feature_names: List[str] = None
    ) -> str:
        """Convert feature and impact to readable language"""
        # This would be customized based on your domain
        # Example implementation:
        direction = "high" if impact > 0 else "low"
        return f"your {feature} is {direction}"

    def explain_with_counterfactual(
        self,
        instance: np.ndarray,
        prediction: int,
        desired_outcome: int = None
    ) -> str:
        """
        Generate explanation with counterfactual (what would need to change)

        Args:
            instance: Input instance
            prediction: Current prediction
            desired_outcome: What outcome is desired (if different)

        Returns:
            Full explanation including counterfactuals
        """
        # Base explanation
        base_explanation = self.explain_to_layperson(instance, prediction)

        # If desired outcome is different, add counterfactual
        if desired_outcome is not None and desired_outcome != prediction:
            counterfactual = self.generate_counterfactual(
                instance, desired_outcome
            )

            cf_text = "\n\nTo achieve a different outcome, consider:\n"
            for change in counterfactual['suggested_changes'][:3]:
                cf_text += f"- {change['suggestion']}\n"

            return base_explanation + cf_text

        return base_explanation
