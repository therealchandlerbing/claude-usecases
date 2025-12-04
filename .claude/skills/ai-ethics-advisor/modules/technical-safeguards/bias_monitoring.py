"""
Comprehensive bias monitoring implementation for AI systems

This module provides tools for detecting, measuring, and monitoring bias
across protected attributes in AI/ML systems.
"""

from typing import Dict, List, Tuple
import numpy as np
from dataclasses import dataclass


@dataclass
class FairnessMetrics:
    """Store fairness metric results"""
    statistical_parity_difference: float
    equalized_odds_difference: float
    equal_opportunity_difference: float
    predictive_parity_difference: float
    disparate_impact_ratio: float


class BiasMonitor:
    """
    Comprehensive bias monitoring for AI systems

    Usage:
        monitor = BiasMonitor(
            protected_attributes=['race', 'gender', 'age'],
            fairness_thresholds={
                'statistical_parity': 0.1,
                'equalized_odds': 0.1,
                'equal_opportunity': 0.1,
                'disparate_impact': 0.8
            }
        )

        results = monitor.evaluate_fairness(
            predictions=predictions,
            actuals=actuals,
            demographics=demographics_dict
        )
    """

    def __init__(
        self,
        protected_attributes: List[str],
        fairness_thresholds: Dict[str, float] = None
    ):
        self.protected_attributes = protected_attributes
        self.thresholds = fairness_thresholds or {
            'statistical_parity': 0.1,
            'equalized_odds': 0.1,
            'equal_opportunity': 0.1,
            'disparate_impact': 0.8,  # 80% rule
        }
        self.violation_log = []

    def evaluate_fairness(
        self,
        predictions: np.ndarray,
        actuals: np.ndarray,
        demographics: Dict[str, np.ndarray],
        probabilities: np.ndarray = None
    ) -> Dict[str, FairnessMetrics]:
        """
        Evaluate fairness metrics across all protected attributes

        Args:
            predictions: Binary predictions (0/1)
            actuals: Ground truth labels (0/1)
            demographics: Dict mapping attribute names to arrays of values
            probabilities: Optional prediction probabilities

        Returns:
            Dict mapping attribute names to fairness metrics
        """
        results = {}

        for attr in self.protected_attributes:
            attr_values = demographics[attr]
            unique_values = np.unique(attr_values)

            if len(unique_values) < 2:
                continue

            # Calculate metrics for each pair of groups
            metrics = self._calculate_pairwise_metrics(
                predictions, actuals, attr_values,
                unique_values, probabilities
            )

            results[attr] = metrics

        # Check for violations and log
        violations = self._flag_violations(results)
        if violations:
            self.violation_log.append({
                'timestamp': self._get_timestamp(),
                'violations': violations
            })

        return results

    def _calculate_pairwise_metrics(
        self,
        predictions: np.ndarray,
        actuals: np.ndarray,
        attribute: np.ndarray,
        groups: np.ndarray,
        probabilities: np.ndarray = None
    ) -> Dict[Tuple[str, str], FairnessMetrics]:
        """
        Calculate fairness metrics between all pairs of groups
        """
        metrics = {}

        for i, group_a in enumerate(groups):
            for group_b in groups[i+1:]:
                mask_a = attribute == group_a
                mask_b = attribute == group_b

                # Statistical Parity Difference
                spd = self._statistical_parity_diff(
                    predictions[mask_a], predictions[mask_b]
                )

                # Equalized Odds Difference
                eod = self._equalized_odds_diff(
                    predictions[mask_a], actuals[mask_a],
                    predictions[mask_b], actuals[mask_b]
                )

                # Equal Opportunity Difference
                eopd = self._equal_opportunity_diff(
                    predictions[mask_a], actuals[mask_a],
                    predictions[mask_b], actuals[mask_b]
                )

                # Predictive Parity Difference
                ppd = self._predictive_parity_diff(
                    predictions[mask_a], actuals[mask_a],
                    predictions[mask_b], actuals[mask_b]
                )

                # Disparate Impact Ratio
                di = self._disparate_impact_ratio(
                    predictions[mask_a], predictions[mask_b]
                )

                metrics[(group_a, group_b)] = FairnessMetrics(
                    statistical_parity_difference=spd,
                    equalized_odds_difference=eod,
                    equal_opportunity_difference=eopd,
                    predictive_parity_difference=ppd,
                    disparate_impact_ratio=di
                )

        return metrics

    def _statistical_parity_diff(
        self, pred_a: np.ndarray, pred_b: np.ndarray
    ) -> float:
        """P(Y_hat=1|A=a) - P(Y_hat=1|A=b)"""
        return pred_a.mean() - pred_b.mean()

    def _equalized_odds_diff(
        self,
        pred_a: np.ndarray, actual_a: np.ndarray,
        pred_b: np.ndarray, actual_b: np.ndarray
    ) -> float:
        """Max difference in TPR and FPR"""
        tpr_a = pred_a[actual_a == 1].mean() if (actual_a == 1).any() else 0
        tpr_b = pred_b[actual_b == 1].mean() if (actual_b == 1).any() else 0
        fpr_a = pred_a[actual_a == 0].mean() if (actual_a == 0).any() else 0
        fpr_b = pred_b[actual_b == 0].mean() if (actual_b == 0).any() else 0

        return max(abs(tpr_a - tpr_b), abs(fpr_a - fpr_b))

    def _equal_opportunity_diff(
        self,
        pred_a: np.ndarray, actual_a: np.ndarray,
        pred_b: np.ndarray, actual_b: np.ndarray
    ) -> float:
        """Difference in TPR"""
        tpr_a = pred_a[actual_a == 1].mean() if (actual_a == 1).any() else 0
        tpr_b = pred_b[actual_b == 1].mean() if (actual_b == 1).any() else 0
        return abs(tpr_a - tpr_b)

    def _predictive_parity_diff(
        self,
        pred_a: np.ndarray, actual_a: np.ndarray,
        pred_b: np.ndarray, actual_b: np.ndarray
    ) -> float:
        """Difference in precision"""
        prec_a = actual_a[pred_a == 1].mean() if (pred_a == 1).any() else 0
        prec_b = actual_b[pred_b == 1].mean() if (pred_b == 1).any() else 0
        return abs(prec_a - prec_b)

    def _disparate_impact_ratio(
        self, pred_a: np.ndarray, pred_b: np.ndarray
    ) -> float:
        """min(P(Y_hat=1|A=a), P(Y_hat=1|A=b)) / max(P(Y_hat=1|A=a), P(Y_hat=1|A=b))"""
        rate_a = pred_a.mean()
        rate_b = pred_b.mean()
        if max(rate_a, rate_b) == 0:
            return 1.0
        return min(rate_a, rate_b) / max(rate_a, rate_b)

    def _flag_violations(
        self, results: Dict[str, Dict[Tuple, FairnessMetrics]]
    ) -> List[Dict]:
        """Identify threshold violations"""
        violations = []

        for attr, metrics_dict in results.items():
            for groups, metrics in metrics_dict.items():
                if abs(metrics.statistical_parity_difference) > \
                   self.thresholds['statistical_parity']:
                    violations.append({
                        'attribute': attr,
                        'groups': groups,
                        'metric': 'statistical_parity',
                        'value': metrics.statistical_parity_difference,
                        'threshold': self.thresholds['statistical_parity']
                    })

                if metrics.disparate_impact_ratio < \
                   self.thresholds['disparate_impact']:
                    violations.append({
                        'attribute': attr,
                        'groups': groups,
                        'metric': 'disparate_impact',
                        'value': metrics.disparate_impact_ratio,
                        'threshold': self.thresholds['disparate_impact']
                    })

        return violations

    def generate_fairness_report(self) -> str:
        """Generate human-readable fairness assessment"""
        # Implementation for report generation
        # Would format violation_log and current metrics into readable report
        pass

    @staticmethod
    def _get_timestamp():
        from datetime import datetime
        return datetime.now().isoformat()
