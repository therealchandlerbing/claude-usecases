"""
Privacy-preserving machine learning implementations

Includes differential privacy and federated learning techniques
for protecting individual privacy while enabling AI development.
"""

from typing import List, Tuple
import numpy as np


class DifferentialPrivacyEngine:
    """
    Apply differential privacy to model training and inference

    Usage:
        dp_engine = DifferentialPrivacyEngine(epsilon=1.0, delta=1e-5)
        noisy_gradients = dp_engine.add_noise_to_gradients(
            gradients, clip_norm=1.0
        )
    """

    def __init__(self, epsilon: float = 1.0, delta: float = 1e-5):
        """
        Initialize DP engine

        Args:
            epsilon: Privacy budget (lower = more private, less accurate)
            delta: Privacy parameter (probability of privacy breach)
        """
        self.epsilon = epsilon
        self.delta = delta

    def add_noise_to_gradients(
        self,
        gradients: np.ndarray,
        clip_norm: float = 1.0
    ) -> np.ndarray:
        """
        Add calibrated noise to gradients (DP-SGD)

        Args:
            gradients: Original gradients
            clip_norm: L2 norm clipping threshold

        Returns:
            Noisy gradients with privacy guarantee
        """
        # Clip gradients
        clipped_grads = self._clip_gradients(gradients, clip_norm)

        # Add Gaussian noise
        noise_scale = self._calculate_noise_scale(clip_norm)
        noise = np.random.normal(0, noise_scale, clipped_grads.shape)

        return clipped_grads + noise

    def _clip_gradients(
        self,
        gradients: np.ndarray,
        clip_norm: float
    ) -> np.ndarray:
        """Clip gradient norms for privacy"""
        grad_norm = np.linalg.norm(gradients)
        if grad_norm > clip_norm:
            return gradients * (clip_norm / grad_norm)
        return gradients

    def _calculate_noise_scale(self, sensitivity: float) -> float:
        """Calculate appropriate noise scale for privacy guarantee"""
        return sensitivity * np.sqrt(2 * np.log(1.25 / self.delta)) / self.epsilon

    def add_noise_to_query_result(
        self,
        query_result: float,
        sensitivity: float
    ) -> float:
        """
        Add noise to query result for differential privacy

        Args:
            query_result: True query result
            sensitivity: Sensitivity of the query (max change from one individual)

        Returns:
            Noisy query result
        """
        noise_scale = self._calculate_noise_scale(sensitivity)
        noise = np.random.normal(0, noise_scale)
        return query_result + noise

    def compute_privacy_budget_spent(
        self,
        num_queries: int,
        composition: str = 'basic'
    ) -> float:
        """
        Compute total privacy budget spent

        Args:
            num_queries: Number of queries made
            composition: 'basic' or 'advanced' composition

        Returns:
            Total epsilon spent
        """
        if composition == 'basic':
            # Basic composition: epsilon adds linearly
            return self.epsilon * num_queries
        elif composition == 'advanced':
            # Advanced composition (approximate)
            # This is simplified; use proper libraries for production
            return self.epsilon * np.sqrt(2 * num_queries * np.log(1/self.delta))
        else:
            raise ValueError(f"Unknown composition: {composition}")


class FederatedLearningCoordinator:
    """
    Coordinate federated learning for privacy-preserving distributed training

    In federated learning, models are trained on local data and only
    model updates (not raw data) are shared with a central server.

    Usage:
        coordinator = FederatedLearningCoordinator(num_clients=10)

        # Clients train locally and send updates
        global_update = coordinator.aggregate_updates(
            client_updates=[update1, update2, ...],
            client_weights=[n1, n2, ...]  # optional: weight by data size
        )

        # Apply to global model
        global_model.apply_update(global_update)
    """

    def __init__(self, num_clients: int):
        self.num_clients = num_clients
        self.global_model = None
        self.round_number = 0

    def aggregate_updates(
        self,
        client_updates: List[np.ndarray],
        client_weights: List[float] = None
    ) -> np.ndarray:
        """
        Aggregate client model updates (Federated Averaging)

        Args:
            client_updates: List of model updates from clients
            client_weights: Optional weights (e.g., by data size)

        Returns:
            Aggregated update
        """
        if client_weights is None:
            # Equal weighting
            client_weights = [1.0 / len(client_updates)] * len(client_updates)

        # Normalize weights
        total_weight = sum(client_weights)
        client_weights = [w / total_weight for w in client_weights]

        # Weighted average of client updates
        aggregated = sum(
            w * update
            for w, update in zip(client_weights, client_updates)
        )

        self.round_number += 1
        return aggregated

    def secure_aggregation(
        self,
        client_updates: List[np.ndarray],
        client_weights: List[float] = None
    ) -> np.ndarray:
        """
        Secure aggregation with added noise for additional privacy

        This adds differential privacy to the aggregation step.

        Args:
            client_updates: List of model updates from clients
            client_weights: Optional weights

        Returns:
            Aggregated update with privacy guarantees
        """
        # Basic aggregation
        aggregated = self.aggregate_updates(client_updates, client_weights)

        # Add noise for differential privacy
        # Sensitivity depends on clipping
        clip_norm = self._calculate_clip_norm(client_updates)
        dp_engine = DifferentialPrivacyEngine(epsilon=1.0, delta=1e-5)
        noisy_aggregated = dp_engine.add_noise_to_gradients(
            aggregated,
            clip_norm=clip_norm
        )

        return noisy_aggregated

    def _calculate_clip_norm(self, updates: List[np.ndarray]) -> float:
        """Calculate appropriate clipping norm"""
        # Simplified: use median of update norms
        norms = [np.linalg.norm(update) for update in updates]
        return float(np.median(norms))

    def client_selection(
        self,
        total_clients: int,
        clients_per_round: int,
        method: str = 'random'
    ) -> List[int]:
        """
        Select clients for this round

        Args:
            total_clients: Total number of available clients
            clients_per_round: How many to select
            method: Selection method ('random', 'round_robin', etc.)

        Returns:
            List of selected client indices
        """
        if method == 'random':
            return list(np.random.choice(
                total_clients,
                size=clients_per_round,
                replace=False
            ))
        elif method == 'round_robin':
            start = (self.round_number * clients_per_round) % total_clients
            indices = [(start + i) % total_clients
                      for i in range(clients_per_round)]
            return indices
        else:
            raise ValueError(f"Unknown selection method: {method}")


class DataMinimizer:
    """
    Tools for data minimization and privacy-preserving transformations
    """

    @staticmethod
    def k_anonymize(
        data: np.ndarray,
        k: int,
        quasi_identifiers: List[int]
    ) -> np.ndarray:
        """
        Apply k-anonymity to dataset

        Ensures each record is indistinguishable from at least k-1 others.

        Args:
            data: Input dataset
            k: Minimum group size
            quasi_identifiers: Indices of quasi-identifying columns

        Returns:
            Anonymized dataset
        """
        # This is a simplified implementation
        # For production, use specialized k-anonymity libraries

        # Generalize quasi-identifiers to achieve k-anonymity
        anonymized = data.copy()

        for qi in quasi_identifiers:
            # Generalize by binning
            unique_values = len(np.unique(data[:, qi]))
            if unique_values > k:
                # Create bins to reduce unique values
                bins = np.linspace(
                    data[:, qi].min(),
                    data[:, qi].max(),
                    num=max(2, unique_values // k)
                )
                anonymized[:, qi] = np.digitize(data[:, qi], bins)

        return anonymized

    @staticmethod
    def aggregate_by_group(
        data: np.ndarray,
        group_size: int = 10
    ) -> np.ndarray:
        """
        Aggregate data into groups to prevent individual re-identification

        Args:
            data: Input data
            group_size: Size of aggregation groups

        Returns:
            Aggregated data
        """
        n_groups = len(data) // group_size
        aggregated = []

        for i in range(n_groups):
            group = data[i*group_size:(i+1)*group_size]
            # Average within group
            aggregated.append(group.mean(axis=0))

        return np.array(aggregated)

    @staticmethod
    def add_random_noise(
        data: np.ndarray,
        noise_level: float = 0.1
    ) -> np.ndarray:
        """
        Add random noise to reduce re-identification risk

        Args:
            data: Input data
            noise_level: Proportion of standard deviation to add as noise

        Returns:
            Data with added noise
        """
        std = data.std(axis=0)
        noise = np.random.normal(
            0,
            noise_level * std,
            size=data.shape
        )
        return data + noise
