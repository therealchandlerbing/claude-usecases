# AI Ethics Implementation Guide

**Making Ethics Operational: From Framework to Practice**

---

## Integration Roadmap

### Phase 1: Foundation (Weeks 1-4)

#### Week 1: Assessment & Planning
- [ ] Review comprehensive AI ethics framework
- [ ] Inventory all AI systems (planned, in development, deployed)
- [ ] Conduct rapid screen on each system
- [ ] Identify high-risk systems requiring immediate comprehensive assessment
- [ ] Form ethics review board

#### Week 2: Setup & Configuration
- [ ] Deploy bias monitoring code in test environment
- [ ] Configure monitoring dashboards
- [ ] Set up alert systems
- [ ] Create document repository for assessments
- [ ] Establish incident response procedures

#### Week 3: Team Training
- [ ] Ethics awareness training for all AI practitioners
- [ ] Deep-dive training for leads on comprehensive assessment
- [ ] Bias testing workshop
- [ ] Incident response drill

#### Week 4: First Deployments
- [ ] Complete first comprehensive assessment
- [ ] Deploy monitoring for highest-risk system
- [ ] Document lessons learned
- [ ] Refine processes based on feedback

### Phase 2: Scale (Months 2-3)

- Integrate ethics checkpoints into development lifecycle
- Automate bias testing in CI/CD pipeline
- Conduct comprehensive assessments for all high-risk systems
- Establish community advisory boards
- Launch public transparency reporting

### Phase 3: Maturity (Months 4-6)

- Ethics-by-design becomes default practice
- Real-time monitoring across all systems
- Regular external audits
- Contributing to industry standards
- Proactive ethics research

---

## Development Lifecycle Integration

### Stage 1: Problem Framing & Planning

**Ethics Questions:**
- What problem are we actually solving?
- Who benefits? Who might be harmed?
- Are we solving the right problem or automating the wrong one?
- What would success look like for all stakeholders?

**Deliverables:**
- Stakeholder map
- Ethical considerations document
- Success criteria including equity metrics
- Early engagement plan with affected communities

**Code Example: Problem Framing Template**

```python
"""
Ethical Problem Framing Template
Use this at project inception
"""

class AIProjectFraming:
    def __init__(self):
        self.problem_statement = ""
        self.stakeholders = {}
        self.success_criteria = {}
        self.ethical_considerations = []

    def frame_problem(self):
        """Guide team through ethical problem framing"""
        print("=" * 60)
        print("ETHICAL AI PROJECT FRAMING")
        print("=" * 60)

        self.problem_statement = input("\nWhat problem are we solving? ")

        print("\n--- STAKEHOLDER MAPPING ---")
        self._identify_stakeholders()

        print("\n--- IMPACT ASSESSMENT ---")
        self._assess_impacts()

        print("\n--- ETHICAL RED FLAGS ---")
        self._check_red_flags()

        print("\n--- SUCCESS CRITERIA ---")
        self._define_success()

        self._generate_framing_document()

    def _identify_stakeholders(self):
        """Identify all affected parties"""
        stakeholder_types = [
            "Direct users (who interacts)",
            "Decision subjects (who is decided about)",
            "Affected non-users (indirect impact)",
            "Vulnerable populations (heightened risk)",
            "Operators (who manages system)"
        ]

        for stype in stakeholder_types:
            stakeholder = input(f"{stype}: ")
            if stakeholder:
                impact = input(f"  Impact level (Low/Med/High): ")
                self.stakeholders[stype] = {
                    'groups': stakeholder,
                    'impact': impact
                }

    def _assess_impacts(self):
        """Assess potential impacts across domains"""
        impact_domains = {
            'Economic': 'employment, financial access, resources',
            'Social': 'relationships, community, belonging',
            'Political': 'rights, representation, participation',
            'Health': 'medical care, wellbeing',
            'Educational': 'learning, credentials, opportunities',
            'Legal': 'justice, rights enforcement'
        }

        for domain, examples in impact_domains.items():
            response = input(f"{domain} impact ({examples})? [y/n]: ")
            if response.lower() == 'y':
                detail = input(f"  Describe {domain.lower()} impact: ")
                self.ethical_considerations.append({
                    'domain': domain,
                    'impact': detail
                })

    def _check_red_flags(self):
        """Check for critical ethical concerns"""
        red_flags = [
            "Decisions about children",
            "Vulnerable populations affected",
            "Biometric data used",
            "Criminal justice context",
            "Healthcare decisions",
            "Employment decisions",
            "No human oversight possible",
            "Can't explain decisions",
            "Historical bias in data"
        ]

        print("\nCheck any that apply:")
        flags_found = []
        for i, flag in enumerate(red_flags, 1):
            response = input(f"{i}. {flag}? [y/n]: ")
            if response.lower() == 'y':
                flags_found.append(flag)

        if flags_found:
            print("\n[!] RED FLAGS DETECTED:")
            for flag in flags_found:
                print(f"  - {flag}")
            print("\n[!] COMPREHENSIVE ETHICS ASSESSMENT REQUIRED")

    def _define_success(self):
        """Define success metrics including equity"""
        print("\nDefine success metrics:")

        traditional = input("Traditional metrics (accuracy, speed, etc.): ")
        self.success_criteria['traditional'] = traditional

        equity = input("Equity metrics (fairness across groups): ")
        self.success_criteria['equity'] = equity

        satisfaction = input("User satisfaction (by demographic): ")
        self.success_criteria['satisfaction'] = satisfaction

    def _generate_framing_document(self):
        """Generate problem framing document"""
        doc = f"""
AI PROJECT ETHICAL FRAMING DOCUMENT
{'=' * 60}

PROBLEM STATEMENT
{self.problem_statement}

STAKEHOLDERS
"""
        for stype, details in self.stakeholders.items():
            doc += f"\n{stype}\n  Groups: {details['groups']}\n  Impact: {details['impact']}"

        doc += "\n\nETHICAL CONSIDERATIONS"
        for consideration in self.ethical_considerations:
            doc += f"\n{consideration['domain']}: {consideration['impact']}"

        doc += "\n\nSUCCESS CRITERIA"
        for criterion_type, criterion in self.success_criteria.items():
            doc += f"\n{criterion_type.title()}: {criterion}"

        print("\n" + doc)

        with open('project_ethical_framing.txt', 'w') as f:
            f.write(doc)
        print("\n[OK] Framing document saved")


# Usage
if __name__ == "__main__":
    framing = AIProjectFraming()
    framing.frame_problem()
```

### Stage 2: Data Collection & Preparation

**Ethics Questions:**
- Where did this data come from?
- Who is represented? Who is missing?
- What historical biases might be encoded?
- Do we have consent for this use?

**Required Practices:**
- Data sheet documentation
- Representation analysis
- Bias audit
- Privacy impact assessment

**Code Example: Data Audit Tool**

```python
"""
Data Bias Audit Tool
Analyze training data for representation and quality issues
"""

import pandas as pd
import numpy as np
from typing import Dict, List

class DataBiasAuditor:
    """
    Audit training data for bias and representation issues
    """

    def __init__(self, data: pd.DataFrame, target: str):
        self.data = data
        self.target = target
        self.protected_attributes = []
        self.audit_results = {}

    def register_protected_attributes(self, attributes: List[str]):
        """Register attributes to audit (e.g., race, gender, age)"""
        self.protected_attributes = attributes

    def run_full_audit(self) -> Dict:
        """Run comprehensive bias audit"""
        print("=" * 60)
        print("DATA BIAS AUDIT")
        print("=" * 60)

        results = {
            'representation': self._analyze_representation(),
            'quality': self._analyze_data_quality(),
            'label_distribution': self._analyze_label_distribution(),
            'missing_data': self._analyze_missing_data(),
        }

        self.audit_results = results
        self._generate_audit_report()

        return results

    def _analyze_representation(self) -> Dict:
        """Analyze demographic representation"""
        print("\n--- REPRESENTATION ANALYSIS ---")

        representation = {}

        for attr in self.protected_attributes:
            if attr not in self.data.columns:
                print(f"Warning: {attr} not found in data")
                continue

            counts = self.data[attr].value_counts()
            percentages = self.data[attr].value_counts(normalize=True) * 100

            representation[attr] = {
                'counts': counts.to_dict(),
                'percentages': percentages.to_dict()
            }

            print(f"\n{attr}:")
            for value, pct in percentages.items():
                print(f"  {value}: {pct:.1f}%")

            if percentages.min() < 5:
                print(f"  [!] Warning: Some groups <5% representation")

        return representation

    def _analyze_data_quality(self) -> Dict:
        """Analyze data quality by demographic group"""
        print("\n--- DATA QUALITY ANALYSIS ---")

        quality = {}

        numeric_features = self.data.select_dtypes(
            include=['int64', 'float64']
        ).columns.tolist()

        if self.target in numeric_features:
            numeric_features.remove(self.target)

        for attr in self.protected_attributes:
            if attr not in self.data.columns:
                continue

            print(f"\n{attr}:")
            quality[attr] = {}

            for group in self.data[attr].unique():
                group_data = self.data[self.data[attr] == group]

                completeness = (
                    group_data[numeric_features].notna().sum().sum() /
                    (len(group_data) * len(numeric_features)) * 100
                )

                quality[attr][group] = {
                    'completeness': completeness,
                    'sample_size': len(group_data)
                }

                print(f"  {group}: {completeness:.1f}% complete, n={len(group_data)}")

                if completeness < 80:
                    print(f"    [!] Low completeness")

        return quality

    def _analyze_label_distribution(self) -> Dict:
        """Analyze label distribution across groups"""
        print("\n--- LABEL DISTRIBUTION ANALYSIS ---")

        label_dist = {}

        for attr in self.protected_attributes:
            if attr not in self.data.columns:
                continue

            print(f"\n{attr}:")
            label_dist[attr] = {}

            for group in self.data[attr].unique():
                group_data = self.data[self.data[attr] == group]

                if self.data[self.target].dtype == 'bool' or \
                   self.data[self.target].nunique() == 2:
                    positive_rate = (
                        group_data[self.target].sum() / len(group_data) * 100
                    )
                    label_dist[attr][group] = positive_rate
                    print(f"  {group}: {positive_rate:.1f}% positive labels")

            if label_dist[attr]:
                rates = list(label_dist[attr].values())
                if max(rates) - min(rates) > 20:
                    print(f"  [!] >20% difference in positive rates across groups")

        return label_dist

    def _analyze_missing_data(self) -> Dict:
        """Analyze missing data patterns"""
        print("\n--- MISSING DATA ANALYSIS ---")

        missing = {}

        for attr in self.protected_attributes:
            if attr not in self.data.columns:
                continue

            print(f"\n{attr}:")
            missing[attr] = {}

            for group in self.data[attr].unique():
                group_data = self.data[self.data[attr] == group]
                missing_pct = group_data.isna().sum().sum() / group_data.size * 100

                missing[attr][group] = missing_pct
                print(f"  {group}: {missing_pct:.1f}% missing")

            rates = list(missing[attr].values())
            if max(rates) - min(rates) > 10:
                print(f"  [!] >10% difference in missing data across groups")

        return missing

    def _generate_audit_report(self):
        """Generate comprehensive audit report"""
        print("\n" + "=" * 60)
        print("AUDIT SUMMARY")
        print("=" * 60)

        issues = []

        for attr, data in self.audit_results['representation'].items():
            percentages = list(data['percentages'].values())
            if min(percentages) < 5:
                issues.append(f"Underrepresentation in {attr} (<5% for some groups)")

        for attr, groups in self.audit_results['quality'].items():
            for group, metrics in groups.items():
                if metrics['completeness'] < 80:
                    issues.append(
                        f"Low data quality for {group} in {attr} "
                        f"({metrics['completeness']:.1f}% complete)"
                    )

        for attr, groups in self.audit_results['label_distribution'].items():
            if groups:
                rates = list(groups.values())
                if max(rates) - min(rates) > 20:
                    issues.append(
                        f"Large label imbalance in {attr} "
                        f"({max(rates):.1f}% vs {min(rates):.1f}%)"
                    )

        if issues:
            print("\n[!] ISSUES IDENTIFIED:")
            for i, issue in enumerate(issues, 1):
                print(f"{i}. {issue}")
        else:
            print("\n[OK] No critical issues identified")

        print("\nRECOMMENDATIONS:")
        if len(issues) > 0:
            print("1. Address identified data quality issues before modeling")
            print("2. Consider oversampling underrepresented groups")
            print("3. Document known limitations in model card")
            print("4. Plan for additional data collection if feasible")
            print("5. Implement fairness constraints during training")
        else:
            print("1. Proceed with modeling")
            print("2. Continue monitoring for drift")
            print("3. Document data characteristics in model card")


# Usage Example
if __name__ == "__main__":
    df = pd.read_csv('training_data.csv')

    auditor = DataBiasAuditor(data=df, target='outcome')

    auditor.register_protected_attributes([
        'race', 'gender', 'age_group', 'income_bracket'
    ])

    results = auditor.run_full_audit()
```

### Stage 3: Model Development & Training

**Ethics Checkpoints:**
- Fairness metrics selection
- Bias mitigation techniques
- Explainability requirements
- Privacy-preserving methods

**Code Example: Fairness-Aware Training**

```python
"""
Fairness-Aware Model Training
Integrate fairness constraints into model training
"""

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.linear_model import LogisticRegression
from typing import Dict, List

class FairnessAwareClassifier(BaseEstimator, ClassifierMixin):
    """
    Wrapper that adds fairness constraints to any sklearn classifier
    """

    def __init__(
        self,
        base_estimator=None,
        fairness_constraint='demographic_parity',
        protected_attribute: str = None,
        epsilon: float = 0.05
    ):
        """
        Args:
            base_estimator: sklearn classifier
            fairness_constraint: 'demographic_parity', 'equal_opportunity', 'equalized_odds'
            protected_attribute: column name of protected attribute
            epsilon: acceptable fairness violation (0.05 = 5%)
        """
        self.base_estimator = base_estimator or LogisticRegression()
        self.fairness_constraint = fairness_constraint
        self.protected_attribute = protected_attribute
        self.epsilon = epsilon
        self.group_thresholds = {}

    def fit(self, X, y, sensitive_features=None):
        """
        Train model with fairness constraints
        """
        if sensitive_features is None:
            if self.protected_attribute is None:
                raise ValueError("Must provide sensitive_features or protected_attribute")
            sensitive_features = X[self.protected_attribute]
            X_train = X.drop(columns=[self.protected_attribute])
        else:
            X_train = X

        self.base_estimator.fit(X_train, y)

        if self.fairness_constraint != 'none':
            self._calibrate_thresholds(X_train, y, sensitive_features)

        return self

    def predict(self, X, sensitive_features=None):
        """
        Make fair predictions using group-specific thresholds
        """
        if sensitive_features is None:
            if self.protected_attribute is None:
                return self.base_estimator.predict(X)
            sensitive_features = X[self.protected_attribute]
            X_pred = X.drop(columns=[self.protected_attribute])
        else:
            X_pred = X

        proba = self.base_estimator.predict_proba(X_pred)[:, 1]

        predictions = np.zeros(len(proba))
        for group in self.group_thresholds:
            mask = (sensitive_features == group)
            threshold = self.group_thresholds[group]
            predictions[mask] = (proba[mask] >= threshold).astype(int)

        return predictions

    def _calibrate_thresholds(self, X, y, sensitive_features):
        """
        Calculate group-specific thresholds to achieve fairness
        """
        proba = self.base_estimator.predict_proba(X)[:, 1]
        unique_groups = np.unique(sensitive_features)

        if self.fairness_constraint == 'demographic_parity':
            target_rate = proba.mean()

            for group in unique_groups:
                mask = (sensitive_features == group)
                group_proba = proba[mask]
                threshold = np.percentile(group_proba, (1 - target_rate) * 100)
                self.group_thresholds[group] = threshold

        elif self.fairness_constraint == 'equal_opportunity':
            positive_mask = (y == 1)
            target_tpr = np.mean(proba[positive_mask] >= 0.5)

            for group in unique_groups:
                mask = (sensitive_features == group) & positive_mask
                if mask.sum() > 0:
                    group_proba = proba[mask]
                    threshold = np.percentile(group_proba, (1 - target_tpr) * 100)
                    self.group_thresholds[group] = threshold
                else:
                    self.group_thresholds[group] = 0.5

        elif self.fairness_constraint == 'equalized_odds':
            for group in unique_groups:
                self.group_thresholds[group] = 0.5


# Usage
if __name__ == "__main__":
    from sklearn.model_selection import train_test_split
    import pandas as pd

    df = pd.read_csv('training_data.csv')
    X = df.drop(columns=['outcome'])
    y = df['outcome']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    fair_clf = FairnessAwareClassifier(
        protected_attribute='race',
        fairness_constraint='demographic_parity',
        epsilon=0.05
    )

    fair_clf.fit(X_train, y_train)
```

### Stage 4: Testing & Validation

**Required Tests:**
- Unit tests for bias monitoring code
- Integration tests for fairness constraints
- Edge case testing across demographics
- Adversarial bias testing
- User acceptance testing with diverse participants

### Stage 5: Deployment

**Code Example: Pre-Deployment Checker**

```python
"""
Pre-Deployment Ethics Checklist
Automated checks before production deployment
"""

import os
from typing import Dict, List

class PreDeploymentChecker:
    def __init__(self, model, test_data, config):
        self.model = model
        self.test_data = test_data
        self.config = config
        self.checks_passed = []
        self.checks_failed = []

    def run_all_checks(self) -> bool:
        """Run all pre-deployment checks"""
        print("=" * 60)
        print("PRE-DEPLOYMENT ETHICS CHECKLIST")
        print("=" * 60)

        checks = [
            self._check_documentation,
            self._check_fairness_metrics,
            self._check_performance_thresholds,
            self._check_monitoring_setup,
            self._check_human_oversight,
            self._check_incident_response,
            self._check_approvals
        ]

        for check in checks:
            check()

        self._print_summary()

        return len(self.checks_failed) == 0

    def _check_documentation(self):
        """Verify required documentation exists"""
        print("\n[1/7] Checking documentation...")

        required_docs = [
            'model_card.md',
            'data_sheet.md',
            'ethics_assessment.md',
            'monitoring_plan.md'
        ]

        missing = [doc for doc in required_docs
                   if not os.path.exists(doc)]

        if missing:
            self.checks_failed.append(
                f"Missing documentation: {', '.join(missing)}"
            )
            print("  [X] FAILED: Missing documentation")
        else:
            self.checks_passed.append("Documentation complete")
            print("  [OK] PASSED")

    def _check_fairness_metrics(self):
        """Verify fairness metrics meet thresholds"""
        print("\n[2/7] Checking fairness metrics...")

        # Import your bias monitor
        # from bias_monitor import BiasMonitor

        # monitor = BiasMonitor(
        #     protected_attributes=self.config['protected_attributes']
        # )

        # results = monitor.evaluate_fairness(
        #     predictions=self.model.predict(self.test_data['X']),
        #     actuals=self.test_data['y'],
        #     demographics=self.test_data['demographics']
        # )

        # violations = monitor.violation_log

        violations = []  # Placeholder

        if violations:
            self.checks_failed.append(
                f"Fairness violations detected: {len(violations)}"
            )
            print("  [X] FAILED: Fairness violations")
        else:
            self.checks_passed.append("Fairness metrics within thresholds")
            print("  [OK] PASSED")

    def _check_performance_thresholds(self):
        """Verify performance meets minimum standards"""
        print("\n[3/7] Checking performance thresholds...")

        from sklearn.metrics import accuracy_score, f1_score

        predictions = self.model.predict(self.test_data['X'])
        actuals = self.test_data['y']

        accuracy = accuracy_score(actuals, predictions)
        f1 = f1_score(actuals, predictions, average='weighted')

        min_accuracy = self.config.get('min_accuracy', 0.70)
        min_f1 = self.config.get('min_f1', 0.70)

        if accuracy < min_accuracy or f1 < min_f1:
            self.checks_failed.append(
                f"Performance below threshold: "
                f"accuracy={accuracy:.3f} (min={min_accuracy}), "
                f"f1={f1:.3f} (min={min_f1})"
            )
            print("  [X] FAILED: Performance below threshold")
        else:
            self.checks_passed.append(
                f"Performance adequate: accuracy={accuracy:.3f}, f1={f1:.3f}"
            )
            print("  [OK] PASSED")

    def _check_monitoring_setup(self):
        """Verify monitoring infrastructure is configured"""
        print("\n[4/7] Checking monitoring setup...")

        configured = True  # Check your actual monitoring

        if configured:
            self.checks_passed.append("Monitoring infrastructure configured")
            print("  [OK] PASSED")
        else:
            self.checks_failed.append("Monitoring infrastructure not configured")
            print("  [X] FAILED: Monitoring not ready")

    def _check_human_oversight(self):
        """Verify human oversight mechanisms"""
        print("\n[5/7] Checking human oversight...")

        oversight_elements = [
            'override_mechanism',
            'review_process',
            'escalation_path'
        ]

        has_oversight = all(
            elem in self.config for elem in oversight_elements
        )

        if has_oversight:
            self.checks_passed.append("Human oversight configured")
            print("  [OK] PASSED")
        else:
            self.checks_failed.append("Human oversight not fully configured")
            print("  [X] FAILED: Missing oversight elements")

    def _check_incident_response(self):
        """Verify incident response readiness"""
        print("\n[6/7] Checking incident response...")

        required_elements = [
            'incident_response_plan.md',
        ]

        missing = [elem for elem in required_elements
                   if not os.path.exists(elem)]

        if missing:
            self.checks_failed.append(
                f"Incident response incomplete: missing {', '.join(missing)}"
            )
            print("  [X] FAILED: Incident response not ready")
        else:
            self.checks_passed.append("Incident response ready")
            print("  [OK] PASSED")

    def _check_approvals(self):
        """Verify required approvals obtained"""
        print("\n[7/7] Checking approvals...")

        required_approvals = [
            'ethics_board',
            'legal',
            'system_owner'
        ]

        approvals = self.config.get('approvals', {})
        missing = [a for a in required_approvals if a not in approvals]

        if missing:
            self.checks_failed.append(
                f"Missing approvals: {', '.join(missing)}"
            )
            print("  [X] FAILED: Approvals incomplete")
        else:
            self.checks_passed.append("All approvals obtained")
            print("  [OK] PASSED")

    def _print_summary(self):
        """Print check summary"""
        print("\n" + "=" * 60)
        print("DEPLOYMENT READINESS SUMMARY")
        print("=" * 60)

        print(f"\n[OK] Passed: {len(self.checks_passed)}")
        for check in self.checks_passed:
            print(f"  - {check}")

        if self.checks_failed:
            print(f"\n[X] Failed: {len(self.checks_failed)}")
            for check in self.checks_failed:
                print(f"  - {check}")

            print("\n[!] DEPLOYMENT BLOCKED")
            print("Address failed checks before deploying to production.")
        else:
            print("\n[OK] ALL CHECKS PASSED")
            print("System ready for deployment.")
```

### Stage 6: Production Monitoring

**Code Example: Production Monitoring Service**

```python
"""
Production Bias Monitoring Service
Real-time fairness monitoring in production
"""

import time
from datetime import datetime, timedelta
import json
from typing import Dict, List
import logging

class ProductionBiasMonitor:
    """
    Continuously monitor production AI system for bias
    """

    def __init__(self, config: Dict):
        self.config = config
        self.alert_history = []
        self.metrics_cache = []
        self.setup_logging()

    def setup_logging(self):
        """Configure logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('bias_monitoring.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def monitor_continuous(self, check_interval_minutes: int = 60):
        """
        Run continuous monitoring loop
        """
        self.logger.info("Starting continuous bias monitoring")

        while True:
            try:
                self._run_monitoring_cycle()
                time.sleep(check_interval_minutes * 60)
            except KeyboardInterrupt:
                self.logger.info("Monitoring stopped by user")
                break
            except Exception as e:
                self.logger.error(f"Monitoring error: {str(e)}")
                time.sleep(60)

    def _run_monitoring_cycle(self):
        """Execute one monitoring cycle"""
        self.logger.info("Running monitoring cycle")

        recent_data = self._fetch_recent_predictions()

        if not recent_data or len(recent_data) == 0:
            self.logger.warning("No recent predictions to analyze")
            return

        metrics = self._calculate_fairness_metrics(recent_data)

        self.metrics_cache.append({
            'timestamp': datetime.now().isoformat(),
            'metrics': metrics
        })

        violations = self._check_violations(metrics)

        if violations:
            self._handle_violations(violations)

        self._send_monitoring_report(metrics, violations)

    def _fetch_recent_predictions(self) -> Dict:
        """
        Fetch recent predictions from production
        Override with actual data fetching logic
        """
        return {
            'predictions': [],
            'actuals': [],
            'demographics': {}
        }

    def _calculate_fairness_metrics(self, data: Dict) -> Dict:
        """Calculate current fairness metrics"""
        # Use BiasMonitor from SKILL.md
        pass

    def _check_violations(self, metrics: Dict) -> List[Dict]:
        """Check for threshold violations"""
        violations = []
        thresholds = self.config['thresholds']
        # Implementation
        return violations

    def _calculate_severity(self, value: float, threshold: float) -> str:
        """Calculate violation severity"""
        ratio = abs(value) / threshold

        if ratio >= 3:
            return 'CRITICAL'
        elif ratio >= 2:
            return 'HIGH'
        elif ratio >= 1.5:
            return 'MEDIUM'
        else:
            return 'LOW'

    def _handle_violations(self, violations: List[Dict]):
        """Handle detected violations"""
        for violation in violations:
            self.logger.warning(f"Violation detected: {violation}")

            if violation['severity'] in ['CRITICAL', 'HIGH']:
                self._send_alert(violation)

            self.alert_history.append({
                'timestamp': datetime.now().isoformat(),
                'violation': violation
            })

    def _send_alert(self, violation: Dict):
        """Send alert for violation"""
        alert_message = f"""
BIAS ALERT - {violation['severity']}

Type: {violation['type']}
Attribute: {violation['attribute']}
Groups: {violation['groups']}
Value: {violation['value']:.4f}
Threshold: {violation['threshold']:.4f}

Detected: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Action required: Review and investigate immediately.
"""

        self.logger.error(alert_message)

    def _send_monitoring_report(self, metrics: Dict, violations: List[Dict]):
        """Send regular monitoring report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'violations': violations,
            'status': 'ALERT' if violations else 'OK'
        }

        with open('monitoring_report.json', 'w') as f:
            json.dump(report, f, indent=2)

        self.logger.info(f"Monitoring report generated: {report['status']}")


# Configuration
config = {
    'protected_attributes': ['race', 'gender', 'age_group'],
    'thresholds': {
        'statistical_parity': 0.10,
        'equalized_odds': 0.10,
        'equal_opportunity': 0.10,
        'disparate_impact': 0.80
    },
    'alert_channels': {
        'email': 'ethics-team@example.com',
        'slack': 'https://hooks.slack.com/services/YOUR/WEBHOOK',
    }
}

# Usage
if __name__ == "__main__":
    monitor = ProductionBiasMonitor(config)
    monitor.monitor_continuous(check_interval_minutes=60)
```

---

## Integration with CI/CD Pipeline

```yaml
# .github/workflows/ai-ethics-checks.yml
# GitHub Actions workflow for automated ethics checks

name: AI Ethics Checks

on:
  pull_request:
    branches: [ main ]
  push:
    branches: [ main ]

jobs:
  ethics-check:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install fairlearn aif360

    - name: Run data bias audit
      run: |
        python scripts/data_bias_audit.py

    - name: Run fairness tests
      run: |
        pytest tests/test_fairness.py -v

    - name: Check documentation
      run: |
        python scripts/check_documentation.py

    - name: Generate ethics report
      run: |
        python scripts/generate_ethics_report.py

    - name: Upload report
      uses: actions/upload-artifact@v2
      with:
        name: ethics-report
        path: ethics_report.html

    - name: Comment on PR
      if: github.event_name == 'pull_request'
      uses: actions/github-script@v5
      with:
        script: |
          const fs = require('fs');
          const report = fs.readFileSync('ethics_report.txt', 'utf8');
          github.rest.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: '## AI Ethics Check Results\n\n' + report
          });
```

---

## Key Success Factors

1. **Executive Sponsorship**
   - Ethics work needs visible leadership support
   - Resource allocation for ethics team
   - Ethics metrics in performance reviews

2. **Cross-Functional Collaboration**
   - Engineers, ethicists, domain experts, legal, affected communities
   - Regular sync meetings
   - Shared accountability

3. **Continuous Learning**
   - Stay current on research and regulations
   - Learn from incidents (yours and industry)
   - Adapt frameworks as you learn

4. **Cultural Change**
   - Ethics is everyone's job, not just ethics team
   - Psychological safety to raise concerns
   - Reward ethical decision-making

5. **Measurement & Accountability**
   - Track ethics metrics
   - Regular audits
   - Transparent reporting
   - Consequences for violations

---

## Quick Start Checklist

**Week 1:**
- [ ] Read Quick Reference Guide
- [ ] Inventory all AI systems
- [ ] Run rapid screens
- [ ] Identify high-risk systems

**Week 2:**
- [ ] Review comprehensive framework
- [ ] Complete one comprehensive assessment
- [ ] Deploy bias monitoring code
- [ ] Set up incident response

**Week 3:**
- [ ] Train team on framework
- [ ] Form ethics review board
- [ ] Integrate into development process
- [ ] Configure monitoring dashboards

**Week 4:**
- [ ] Conduct first formal review meeting
- [ ] Generate first monitoring report
- [ ] Document lessons learned
- [ ] Plan for scale

---

**The goal: Make ethical AI development the default, not the exception.**
