# Rocks vs Mines Classification

## Description

This project utilizes machine learning to classify sonar signals as either rocks or mines. The dataset, sourced from the UCI Machine Learning Repository, includes 208 patterns: 111 patterns from sonar signals bounced off metal cylinders (mines) and 97 patterns from sonar signals bounced off rocks. Each pattern is represented by 60 attributes indicating energy within frequency bands over time.

## Features

- **Objective:** Classify sonar signals as rocks or mines.
- **Techniques Used:** Logistic Regression, Support Vector Machine (SVM), k-Nearest Neighbors (k-NN).
- **Performance Metrics:** Accuracy, Precision, Recall, F1-score.

## Tech Stack

- **Programming Language:** Python
- **Libraries:** pandas, numpy, scikit-learn, matplotlib, seaborn
- **Tools:** Jupyter Notebook

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/almostoutlier/Projects.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Projects/Sonar
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook Rocks_vs_Mines.ipynb
   ```
2. Follow the instructions in the notebook to run the data analysis and classification models.

## Analysis

### Data Preprocessing

- **Cleaning:** Handling missing values and outliers.
- **Feature Engineering:** Scaling features, creating new features if necessary.

### Model Training and Evaluation

- **Logistic Regression:** Evaluated using confusion matrix and classification report.
- **Support Vector Machine (SVM):** Evaluated using confusion matrix and classification report.
- **k-Nearest Neighbors (k-NN):** Evaluated using confusion matrix and classification report.

### Results

- **Logistic Regression:**
  - **Accuracy:** 82%
  - **Precision:** 84%
  - **Recall:** 76%
  - **F1-Score:** 79%

## Dataset

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks))
- **Link to Notebook:** [Github Link](https://github.com/almostoutlier/Projects/blob/main/Rocks_vs_Mines.ipynb)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Contact

For any questions or feedback, please contact [@almostoutlier](mailto:alaharivirinchi123@gmail.com) or connect with me on [LinkedIn](https://www.linkedin.com/in/alahari-virinchi/).
