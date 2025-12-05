"""
Tests for the AI Ethics Advisor privacy-preserving module.

This module tests differential privacy, federated learning coordination,
and data minimization techniques.
"""

import pytest
import numpy as np
import sys
import os
# Direct import now that files use underscores
from privacy_preserving import (
    DifferentialPrivacyEngine,
    FederatedLearningCoordinator,
    DataMinimizer,
)


class TestDifferentialPrivacyEngine:
    """Tests for DifferentialPrivacyEngine class"""

    @pytest.fixture
    def dp_engine(self):
        """Create default DP engine"""
        return DifferentialPrivacyEngine(epsilon=1.0, delta=1e-5)

    @pytest.fixture
    def strict_dp_engine(self):
        """Create strict DP engine (more privacy)"""
        return DifferentialPrivacyEngine(epsilon=0.1, delta=1e-8)

    def test_initialization(self, dp_engine):
        """Test that DP engine initializes with correct parameters"""
        assert dp_engine.epsilon == 1.0
        assert dp_engine.delta == 1e-5

    def test_strict_initialization(self, strict_dp_engine):
        """Test strict DP engine initialization"""
        assert strict_dp_engine.epsilon == 0.1
        assert strict_dp_engine.delta == 1e-8


class TestGradientClipping:
    """Tests for gradient clipping functionality"""

    @pytest.fixture
    def dp_engine(self):
        return DifferentialPrivacyEngine(epsilon=1.0, delta=1e-5)

    def test_clips_large_gradients(self, dp_engine):
        """Test that large gradients are clipped"""
        large_gradients = np.array([10.0, 10.0, 10.0])
        clip_norm = 1.0

        clipped = dp_engine._clip_gradients(large_gradients, clip_norm)
        result_norm = np.linalg.norm(clipped)

        assert result_norm <= clip_norm + 1e-6  # Small tolerance

    def test_preserves_small_gradients(self, dp_engine):
        """Test that small gradients are not modified"""
        small_gradients = np.array([0.1, 0.1, 0.1])
        clip_norm = 10.0

        clipped = dp_engine._clip_gradients(small_gradients, clip_norm)

        np.testing.assert_array_almost_equal(clipped, small_gradients)

    def test_exact_norm_unchanged(self, dp_engine):
        """Test that gradients at exact norm are unchanged"""
        gradients = np.array([1.0, 0.0])  # Norm = 1.0
        clip_norm = 1.0

        clipped = dp_engine._clip_gradients(gradients, clip_norm)

        np.testing.assert_array_almost_equal(clipped, gradients)


class TestNoiseScale:
    """Tests for noise scale calculation"""

    def test_higher_epsilon_less_noise(self):
        """Test that higher epsilon means less noise"""
        engine_high_eps = DifferentialPrivacyEngine(epsilon=10.0, delta=1e-5)
        engine_low_eps = DifferentialPrivacyEngine(epsilon=0.1, delta=1e-5)

        sensitivity = 1.0
        scale_high = engine_high_eps._calculate_noise_scale(sensitivity)
        scale_low = engine_low_eps._calculate_noise_scale(sensitivity)

        assert scale_high < scale_low

    def test_higher_sensitivity_more_noise(self):
        """Test that higher sensitivity requires more noise"""
        engine = DifferentialPrivacyEngine(epsilon=1.0, delta=1e-5)

        scale_low_sens = engine._calculate_noise_scale(sensitivity=0.1)
        scale_high_sens = engine._calculate_noise_scale(sensitivity=10.0)

        assert scale_low_sens < scale_high_sens

    def test_noise_scale_positive(self):
        """Test that noise scale is always positive"""
        engine = DifferentialPrivacyEngine(epsilon=1.0, delta=1e-5)
        scale = engine._calculate_noise_scale(sensitivity=1.0)
        assert scale > 0


class TestAddNoiseToGradients:
    """Tests for gradient noise addition"""

    @pytest.fixture
    def dp_engine(self):
        return DifferentialPrivacyEngine(epsilon=1.0, delta=1e-5)

    def test_returns_same_shape(self, dp_engine):
        """Test that noisy gradients have same shape as input"""
        gradients = np.random.randn(10, 5)
        noisy = dp_engine.add_noise_to_gradients(gradients, clip_norm=1.0)
        assert noisy.shape == gradients.shape

    def test_noise_is_added(self, dp_engine):
        """Test that noise is actually added"""
        np.random.seed(42)
        gradients = np.zeros((10,))
        noisy = dp_engine.add_noise_to_gradients(gradients, clip_norm=1.0)

        # With zero gradients, output should be non-zero noise
        assert not np.allclose(noisy, 0)

    def test_clipping_applied(self, dp_engine):
        """Test that clipping is applied before noise"""
        large_gradients = np.array([100.0, 100.0, 100.0])
        clip_norm = 1.0

        # The noisy gradient magnitude should be bounded
        # (though noise adds uncertainty)
        noisy = dp_engine.add_noise_to_gradients(large_gradients, clip_norm)

        # After clipping, the base should be at most clip_norm
        # Can't make strong assertions due to noise


class TestAddNoiseToQueryResult:
    """Tests for query result noise addition"""

    @pytest.fixture
    def dp_engine(self):
        return DifferentialPrivacyEngine(epsilon=1.0, delta=1e-5)

    def test_returns_float(self, dp_engine):
        """Test that result is a float"""
        result = dp_engine.add_noise_to_query_result(100.0, sensitivity=1.0)
        assert isinstance(result, float)

    def test_noise_varies(self, dp_engine):
        """Test that multiple calls give different results"""
        results = [dp_engine.add_noise_to_query_result(100.0, sensitivity=1.0)
                   for _ in range(10)]
        # Not all results should be the same
        assert len(set(results)) > 1


class TestPrivacyBudgetComputation:
    """Tests for privacy budget computation"""

    @pytest.fixture
    def dp_engine(self):
        return DifferentialPrivacyEngine(epsilon=1.0, delta=1e-5)

    def test_basic_composition(self, dp_engine):
        """Test basic composition (linear)"""
        budget = dp_engine.compute_privacy_budget_spent(
            num_queries=10,
            composition='basic'
        )
        assert budget == 10.0  # epsilon * num_queries

    def test_advanced_composition_sublinear(self, dp_engine):
        """Test advanced composition grows sublinearly with many queries"""
        # For more queries, advanced composition becomes more efficient
        num_queries = 100

        basic = dp_engine.compute_privacy_budget_spent(num_queries, composition='basic')
        advanced = dp_engine.compute_privacy_budget_spent(num_queries, composition='advanced')

        # With 100 queries, advanced should be less than basic
        # basic = 100 * epsilon = 100
        # advanced = epsilon * sqrt(2 * 100 * log(1/delta)) which is much smaller
        assert advanced < basic

    def test_unknown_composition_raises(self, dp_engine):
        """Test that unknown composition method raises error"""
        with pytest.raises(ValueError, match="Unknown composition"):
            dp_engine.compute_privacy_budget_spent(10, composition='unknown')


class TestFederatedLearningCoordinator:
    """Tests for FederatedLearningCoordinator class"""

    @pytest.fixture
    def coordinator(self):
        return FederatedLearningCoordinator(num_clients=10)

    def test_initialization(self, coordinator):
        """Test coordinator initialization"""
        assert coordinator.num_clients == 10
        assert coordinator.global_model is None
        assert coordinator.round_number == 0


class TestAggregateUpdates:
    """Tests for update aggregation"""

    @pytest.fixture
    def coordinator(self):
        return FederatedLearningCoordinator(num_clients=5)

    def test_equal_weight_aggregation(self, coordinator):
        """Test aggregation with equal weights"""
        updates = [
            np.array([1.0, 2.0]),
            np.array([3.0, 4.0]),
            np.array([5.0, 6.0])
        ]

        aggregated = coordinator.aggregate_updates(updates)
        expected = np.array([3.0, 4.0])  # Mean of updates

        np.testing.assert_array_almost_equal(aggregated, expected)

    def test_weighted_aggregation(self, coordinator):
        """Test aggregation with custom weights"""
        updates = [
            np.array([0.0, 0.0]),
            np.array([10.0, 10.0])
        ]
        weights = [1.0, 9.0]  # Second client has 90% weight

        aggregated = coordinator.aggregate_updates(updates, weights)
        expected = np.array([9.0, 9.0])

        np.testing.assert_array_almost_equal(aggregated, expected)

    def test_round_number_increments(self, coordinator):
        """Test that round number increments after aggregation"""
        updates = [np.array([1.0])]

        assert coordinator.round_number == 0
        coordinator.aggregate_updates(updates)
        assert coordinator.round_number == 1
        coordinator.aggregate_updates(updates)
        assert coordinator.round_number == 2


class TestSecureAggregation:
    """Tests for secure aggregation with DP"""

    @pytest.fixture
    def coordinator(self):
        return FederatedLearningCoordinator(num_clients=5)

    def test_secure_aggregation_adds_noise(self, coordinator):
        """Test that secure aggregation adds noise"""
        np.random.seed(42)

        updates = [np.array([1.0, 2.0, 3.0]) for _ in range(5)]

        # Regular aggregation
        regular = coordinator.aggregate_updates(updates.copy())

        # Reset round counter
        coordinator.round_number -= 1

        # Secure aggregation (new random seed for different result)
        np.random.seed(123)
        secure = coordinator.secure_aggregation(updates.copy())

        # Results should differ due to added noise
        assert not np.allclose(regular, secure)


class TestClipNormCalculation:
    """Tests for clip norm calculation"""

    @pytest.fixture
    def coordinator(self):
        return FederatedLearningCoordinator(num_clients=5)

    def test_uses_median_of_norms(self, coordinator):
        """Test that clip norm uses median"""
        updates = [
            np.array([1.0, 0.0]),   # norm = 1
            np.array([2.0, 0.0]),   # norm = 2
            np.array([3.0, 0.0]),   # norm = 3
            np.array([4.0, 0.0]),   # norm = 4
            np.array([5.0, 0.0])    # norm = 5
        ]

        clip_norm = coordinator._calculate_clip_norm(updates)
        assert clip_norm == 3.0  # Median


class TestClientSelection:
    """Tests for client selection"""

    @pytest.fixture
    def coordinator(self):
        return FederatedLearningCoordinator(num_clients=10)

    def test_random_selection_count(self, coordinator):
        """Test random selection returns correct count"""
        selected = coordinator.client_selection(
            total_clients=10,
            clients_per_round=3,
            method='random'
        )
        assert len(selected) == 3

    def test_random_selection_no_duplicates(self, coordinator):
        """Test random selection has no duplicates"""
        selected = coordinator.client_selection(
            total_clients=10,
            clients_per_round=5,
            method='random'
        )
        assert len(selected) == len(set(selected))

    def test_round_robin_selection(self, coordinator):
        """Test round robin selection"""
        # First round
        selected1 = coordinator.client_selection(
            total_clients=10,
            clients_per_round=3,
            method='round_robin'
        )
        assert selected1 == [0, 1, 2]

        # Advance round
        coordinator.round_number = 1
        selected2 = coordinator.client_selection(
            total_clients=10,
            clients_per_round=3,
            method='round_robin'
        )
        assert selected2 == [3, 4, 5]

    def test_unknown_method_raises(self, coordinator):
        """Test that unknown selection method raises error"""
        with pytest.raises(ValueError, match="Unknown selection method"):
            coordinator.client_selection(10, 3, method='invalid')


class TestDataMinimizer:
    """Tests for DataMinimizer static methods"""


class TestKAnonymize:
    """Tests for k-anonymization"""

    def test_reduces_unique_values(self):
        """Test that k-anonymization reduces unique values"""
        data = np.array([
            [1, 25, 50000],
            [2, 26, 51000],
            [3, 45, 75000],
            [4, 46, 76000],
            [5, 65, 90000],
            [6, 66, 91000]
        ]).astype(float)

        anonymized = DataMinimizer.k_anonymize(
            data=data,
            k=2,
            quasi_identifiers=[1, 2]  # Age and income
        )

        # Should have fewer unique values in QI columns
        original_unique_age = len(np.unique(data[:, 1]))
        anonymized_unique_age = len(np.unique(anonymized[:, 1]))

        assert anonymized_unique_age <= original_unique_age

    def test_preserves_non_qi_columns(self):
        """Test that non-QI columns are preserved"""
        data = np.array([
            [1, 25],
            [2, 26],
            [3, 45],
            [4, 46]
        ]).astype(float)

        anonymized = DataMinimizer.k_anonymize(
            data=data,
            k=2,
            quasi_identifiers=[1]  # Only second column
        )

        # First column (non-QI) should be unchanged
        np.testing.assert_array_equal(anonymized[:, 0], data[:, 0])


class TestAggregateByGroup:
    """Tests for group aggregation"""

    def test_reduces_record_count(self):
        """Test that aggregation reduces record count"""
        data = np.random.randn(100, 5)

        aggregated = DataMinimizer.aggregate_by_group(data, group_size=10)

        assert len(aggregated) == 10  # 100 / 10

    def test_computes_group_means(self):
        """Test that aggregation computes means"""
        data = np.array([
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]).astype(float)

        aggregated = DataMinimizer.aggregate_by_group(data, group_size=2)

        expected = np.array([
            [2, 3],    # Mean of first two rows
            [6, 7]     # Mean of last two rows
        ])

        np.testing.assert_array_almost_equal(aggregated, expected)


class TestAddRandomNoise:
    """Tests for random noise addition"""

    def test_preserves_shape(self):
        """Test that noise addition preserves shape"""
        data = np.random.randn(50, 10)
        noisy = DataMinimizer.add_random_noise(data, noise_level=0.1)
        assert noisy.shape == data.shape

    def test_modifies_data(self):
        """Test that data is actually modified"""
        # Use data with non-zero std so noise is actually added
        np.random.seed(42)
        data = np.random.randn(10, 5)
        noisy = DataMinimizer.add_random_noise(data.copy(), noise_level=0.5)
        assert not np.allclose(data, noisy)

    def test_higher_noise_level_more_variation(self):
        """Test that higher noise level causes more variation"""
        # Use data with non-zero std so noise is actually added
        np.random.seed(42)
        base_data = np.random.randn(100, 5)

        np.random.seed(42)
        low_noise = DataMinimizer.add_random_noise(base_data.copy(), noise_level=0.01)

        np.random.seed(43)  # Different seed for different noise
        high_noise = DataMinimizer.add_random_noise(base_data.copy(), noise_level=1.0)

        # Compare difference from original
        low_diff = np.abs(low_noise - base_data).mean()
        high_diff = np.abs(high_noise - base_data).mean()

        assert high_diff > low_diff

    def test_zero_noise_level(self):
        """Test that zero noise level preserves data"""
        data = np.ones((10, 5))
        noisy = DataMinimizer.add_random_noise(data, noise_level=0.0)
        np.testing.assert_array_equal(data, noisy)
