# Flight Delay Prediction

## Description

- **Dataset:** Information about flights in three modules: Airlines, Airports, and Flights.
- **Flights Module:** Includes flight details, departure and arrival airports, delays, cancellations, and reasons.
- **Objectives:**
  - **Multiclass Classification Model:** Predict if a flight will be on time, delayed, or cancelled.
    - **Confusion Matrix on Test Data:**
      ```
                precision    recall  f1-score   support
           C       1.00      1.00      1.00        99
           D       0.94      0.95      0.94      1789
           N       0.99      0.99      0.99      8125
      ```

      ```
      accuracy                           0.98     10013
      ```
   ![alt text](/FlightDelay/image-1.png)

  - **Multilabel Classification Model:** If delayed, predict the delay in minutes.
    - **Confusion Matrix on Test Data:**
      - **Accuracy Score:** 0.856
      - **Hamming Loss:** 0.05
      - **Detailed Results:**
        ```
        AIR_SYSTEM_DELAY | SECURITY_DELAY | AIRLINE_DELAY | LATE_AIRCRAFT_DELAY | WEATHER_DELAY
        --- | --- | --- | --- | ---
        [[8947  265]  |  [[9997    0]  | [[9156  208]  |   [[8918  275]   |   [[9666   47]
        [ 442  359]]  |  [  16    0]]  |  [ 482  167]]  |   [ 355  465]]   |  [ 261   39]]
        ```
  - **Regression Model:** If cancelled, predict the reason for cancellation.
    - **Results:**
      - Data | RMSE | MAE | MAPE
        --- | --- | --- | ---
        Train | 32.210859 | 24.042234 | 0.444889
        Val | 32.409667 | 24.199183 | 0.449289
        Test | 32.224404 | 24.060442 | 0.441072 
   ![alt text](/FlightDelay/regression.png)

## Tech Stack

- **Programming Language:** Python
- **Libraries:** pandas, numpy, scikit-learn, matplotlib
- **Tools:** Jupyter Notebook


## Data Preprocessing

- **Cleaning:** Handle missing values and outliers.
- **Feature Engineering:** Create new features, normalize/scale features, handle categorical variables.

## Model Training and Evaluation

- **Multiclass Classification Model:** Logistic Regression, Decision Trees, Random Forests.
- **Multilabel Classification Model:** One-vs-Rest strategy with Logistic Regression.
- **Regression Model:** Linear Regression, Decision Tree Regression.
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score, RMSE, MAE, MAPE.

## Dataset

- **Source:** [2015 Flight Delays and Cancellations](https://www.kaggle.com/datasets/usdot/flight-delays?select=flights.csv)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/almostoutlier/Projects.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Projects/FlightDelay
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook Flights_Delay.ipynb
   ```
2. Follow the instructions in the notebook to run the data analysis and prediction models.

## Project Structure

- `Flights_Delay.ipynb`: Main notebook for data analysis and prediction.
- `requirements.txt`: List of required Python libraries.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Contact

For any questions or feedback, please contact [@almostoutlier](alaharivirinchi123@gmail.com) or connect with me on [LinkedIn](https://www.linkedin.com/in/alahari-virinchi/).
