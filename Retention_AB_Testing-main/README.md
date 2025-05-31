
# 📊 Statistical Tests with Python

A Jupyter Notebook project demonstrating the application of key statistical tests using Python. This project covers tests for normality, variance, and mean comparisons, along with visualizations and interpretation.

## Overview

This project provides hands-on examples of statistical tests including:
- **Shapiro-Wilk Test** for normality
- **Levene's Test** for equality of variances
- **t-test** and **ANOVA** for mean comparisons
- **Chi-square Test** for categorical data
- **Visualization** of distributions and test results

The notebook contains explanations, code, and output visualizations to help understand when and how to apply each test.

## Features

- Explanation of each statistical test
- Python implementation with **SciPy** and **statsmodels**
- Visualizations with **Matplotlib** and **Seaborn**
- Real-world datasets for practice
- Interpretation of results

## Tech Stack

- **Python Libraries**: pandas, numpy, scipy, statsmodels, matplotlib, seaborn
- **Development**: Jupyter Notebook

## Project Structure

```
statistical-tests/
├── Statistical Tests.ipynb      # Main Jupyter notebook with code and explanations
├── datasets/                    # Folder for datasets used (if applicable)
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Installation

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/statistical-tests.git
   cd statistical-tests
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `Statistical Tests.ipynb` to:
   - Run statistical tests
   - Visualize results
   - Learn about test assumptions and use cases

## Tests Included

- Shapiro-Wilk Test
- Levene's Test
- t-test (Independent and Paired)
- ANOVA
- Chi-square Test

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
