# Contributing to Applied Data Science Portfolio

**Portfolio Author & Maintainer: Srijan Upadhyay**

Thank you for your interest in contributing to this institutional-grade data science portfolio. This document outlines the standards, processes, and expectations for contributions that maintain the rigorous quality expected in tier-1 financial institutions and enterprise ML environments.

## Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Workflow](#development-workflow)
4. [Code Standards](#code-standards)
5. [Documentation Requirements](#documentation-requirements)
6. [Testing Requirements](#testing-requirements)
7. [Pull Request Process](#pull-request-process)
8. [Research Collaboration](#research-collaboration)

---

## Code of Conduct

This project adheres to professional standards expected in institutional research environments:
- **Respectful Communication:** Constructive, professional, and inclusive
- **Intellectual Integrity:** Proper attribution, citation, and acknowledgment
- **Quality Commitment:** Adherence to best practices and institutional standards
- **Confidentiality:** Respect for proprietary data and trade secrets

Violations will result in immediate removal from the project.

---

## Getting Started

### Prerequisites
- Python 3.10+
- Git version control
- Jupyter Notebook/Lab
- Understanding of ML/DL fundamentals
- Familiarity with institutional best practices

### Environment Setup
```bash
# Clone repository
git clone https://github.com/CodersAcademy006/Applied-Data-Science-Portfolio.git
cd Applied-Data-Science-Portfolio

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development tools

# Install pre-commit hooks
pre-commit install
```

---

## Development Workflow

### Branch Strategy
- `main`: Production-ready, stable releases
- `develop`: Integration branch for features
- `feature/<name>`: Individual feature development
- `bugfix/<name>`: Bug fixes
- `hotfix/<name>`: Critical production fixes

### Workflow Steps
1. Create an issue describing the proposed change
2. Fork the repository (external contributors)
3. Create a feature branch from `develop`
4. Implement changes following code standards
5. Write/update tests and documentation
6. Commit with descriptive messages (conventional commits)
7. Push to your fork and create a pull request
8. Address code review feedback
9. Merge upon approval from Srijan Upadhyay

---

## Code Standards

### Python Style Guide
- **PEP 8 Compliance:** Enforced via `black` (line length: 100) and `flake8`
- **Import Order:** Enforced via `isort` (profile: black)
- **Type Hints:** Required for all function signatures (`mypy` validation)
- **Docstrings:** Google style for all public functions, classes, modules

### Example
```python
from typing import List, Tuple

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    hyperparameters: dict,
) -> Tuple[RandomForestClassifier, dict]:
    """
    Train a Random Forest classifier with specified hyperparameters.

    Implements stratified cross-validation for robust performance estimation.
    Hyperparameters are tuned via Bayesian optimization (Optuna).

    Args:
        X_train: Training feature matrix (n_samples, n_features).
        y_train: Training target vector (n_samples,).
        hyperparameters: Model hyperparameters (n_estimators, max_depth, etc.).

    Returns:
        Tuple containing:
            - Trained RandomForestClassifier instance
            - Dictionary with performance metrics (accuracy, precision, recall, F1)

    Raises:
        ValueError: If X_train and y_train have mismatched lengths.

    Example:
        >>> model, metrics = train_model(X_train, y_train, {'n_estimators': 100})
        >>> print(f"Accuracy: {metrics['accuracy']:.3f}")
    """
    if len(X_train) != len(y_train):
        raise ValueError("X_train and y_train must have the same length")
    
    model = RandomForestClassifier(**hyperparameters, random_state=42)
    model.fit(X_train, y_train)
    
    # Calculate metrics...
    metrics = {"accuracy": 0.95, "precision": 0.94, "recall": 0.96}
    
    return model, metrics
```

### Jupyter Notebook Standards
- **Clear Structure:** Markdown headers for sections
- **Cell Order:** Imports → Configuration → Data Loading → EDA → Modeling → Evaluation → Conclusions
- **Output Management:** Clear outputs before committing (use `nbstripout`)
- **Runtime:** Keep cell execution times reasonable (<5 minutes per cell)
- **Reproducibility:** Set random seeds, document environment

---

## Documentation Requirements

### README Files
Every project must include a comprehensive README with:
1. **Header:** Project title, author (Srijan Upadhyay), badges
2. **Executive Summary:** Business context, objectives, impact
3. **Methodology:** Detailed technical approach, algorithms, assumptions
4. **Results:** Performance metrics, visualizations, key insights
5. **Business Value:** Quantified impact, stakeholder recommendations
6. **Technical Stack:** Libraries, tools, infrastructure
7. **Getting Started:** Installation, usage instructions
8. **Future Enhancements:** Planned improvements, scalability
9. **Footer:** Author credit, licensing, contact information

### Inline Documentation
- **Complex Logic:** Explain non-obvious algorithms, optimizations
- **Domain Knowledge:** Provide context for domain-specific terms
- **References:** Cite papers, documentation, blog posts

---

## Testing Requirements

### Unit Tests
- **Coverage:** Minimum 70% for new code
- **Framework:** pytest with fixtures and parametrization
- **Scope:** Core functions, data processing, feature engineering

### Integration Tests
- **Pipeline Tests:** End-to-end workflow validation
- **Data Quality:** Schema validation, null checks, range constraints
- **Model Performance:** Baseline thresholds, regression detection

### Example
```python
import pytest
import pandas as pd
from src.preprocessing import clean_data


@pytest.fixture
def sample_data():
    """Generate sample dataset for testing."""
    return pd.DataFrame({
        'feature1': [1, 2, None, 4],
        'feature2': ['a', 'b', 'c', 'd'],
        'target': [0, 1, 0, 1]
    })


def test_clean_data_removes_nulls(sample_data):
    """Test that clean_data removes rows with null values."""
    result = clean_data(sample_data, handle_nulls='drop')
    assert result.shape[0] == 3
    assert result.isnull().sum().sum() == 0


def test_clean_data_imputes_nulls(sample_data):
    """Test that clean_data imputes null values correctly."""
    result = clean_data(sample_data, handle_nulls='impute', strategy='median')
    assert result.isnull().sum().sum() == 0
    assert result.shape[0] == 4
```

---

## Pull Request Process

### PR Checklist
- [ ] Branch from `develop` (or `main` for hotfixes)
- [ ] Code follows style guide (black, flake8, isort, mypy)
- [ ] All tests pass (pytest, CI pipeline)
- [ ] Documentation updated (README, docstrings, inline comments)
- [ ] No merge conflicts with target branch
- [ ] Descriptive PR title and description
- [ ] Linked to relevant issue(s)
- [ ] Requested review from Srijan Upadhyay

### PR Description Template
```markdown
## Summary
Brief description of changes and motivation.

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to break)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Technical Details
- Algorithm/approach used
- Key design decisions
- Trade-offs considered

## Business Impact
- Expected improvement in KPIs
- Stakeholder value proposition
- Potential risks

## Testing
- Unit tests added/updated
- Integration tests run
- Manual testing performed

## Documentation
- README updated
- Docstrings added
- Inline comments for complex logic

## Related Issues
Closes #<issue_number>
```

### Review Process
1. **Automated Checks:** CI pipeline (linting, testing, security)
2. **Code Review:** At least one approval from Srijan Upadhyay
3. **Documentation Review:** Clarity, completeness, accuracy
4. **Merge:** Squash and merge to maintain clean history

---

## Research Collaboration

### Academic Partnerships
For joint research projects, white-paper co-authorship, or conference submissions:
- **Proposal:** Submit detailed research proposal via GitHub issue
- **Alignment:** Demonstrate relevance to portfolio domains
- **Expertise:** Provide evidence of complementary skills/resources
- **Timeline:** Realistic milestones and deliverables
- **Attribution:** Agree on authorship order and IP rights

### Industry Partnerships
For consulting engagements, model validation, or production deployment:
- **Scope:** Define clear deliverables and success criteria
- **Compliance:** Ensure adherence to regulatory standards
- **Confidentiality:** Sign NDA if proprietary data involved
- **Compensation:** Discuss commercial terms separately

### Contact
For high-level collaboration inquiries, contact Srijan Upadhyay via:
- GitHub: [@CodersAcademy006](https://github.com/CodersAcademy006)
- Portfolio: [Applied-Data-Science-Portfolio](https://github.com/CodersAcademy006/Applied-Data-Science-Portfolio)

---

## Acknowledgments

All contributors will be acknowledged in:
- Project README files
- Repository contributors list
- Derivative publications (if applicable)

Significant contributions may warrant:
- Co-authorship on research papers
- Named recognition in documentation
- Shared intellectual property rights

---

**Maintained By:** Srijan Upadhyay  
**Quality Standards:** Institutional-Grade | Production-Ready | Audit-Compliant  
**Last Updated:** 2024

Thank you for helping maintain the excellence of this portfolio! 🚀
