# Housing Price Prediction with Random Forest Regression

## About the Project

This project constructs and evaluates a predictive model for housing prices using Random Forest Regression. The model is trained on a dataset of housing features, and is implemented using scikit-learn. The goal is to accurately estimate the sale prices of houses based on features like lot area, overall quality, year built, total basement square footage, and above-ground living area.

## How It Works

1.  **Data Loading**: The script loads housing data from `train.csv` and `test.csv` using pandas.
2.  **Feature Selection**: It selects features such as `LotArea`, `OverallQual`, `YearBuilt`, `TotalBsmtSF`, and `GrLivArea` for training the model. The target variable is `SalePrice`.
3.  **Data Splitting**: The training data is split into training and validation sets using scikit-learn's `train_test_split` function.
4.  **Model Training**: A Random Forest Regressor model is trained on the training data using 100 estimators.
5.  **Prediction**: The trained model is used to predict sale prices on the validation set and the test data.
6.  **Evaluation**: The performance of the model is evaluated on the validation set using Mean Absolute Error (MAE).
7.  **Submission**: The predicted sale prices for the test data are saved into a submission file in CSV format.

## Getting Started

### Prerequisites

*   Python 3.x
*   pandas
*   scikit-learn
*   numpy

Install the necessary Python libraries:

pip install pandas scikit-learn numpy

Download the datasets:

1.  Download the `train.csv` and `test.csv` files from [Kaggle's House Prices Competition](https://www.kaggle.com/c/home-data-for-ml-course/data).
2.  Place `train.csv` and `test.csv` in the same directory as `housing_prices.py`.

### Installation

1.  Clone the repository:

git clone https://github.com/BernardoMarta/Housing_prices
cd Housing_Prices

2.  Ensure the `train.csv` and `test.csv` files are in the same directory.

## Usage

Run the script from the command line:

python housing_prices.py


The script will:

1.  Train the model.
2.  Calculate and print the Mean Absolute Error (MAE) on the validation set.
3.  Generate a `submission.csv` file with predicted housing prices for the test data.

## Example

**Input:**

Ensure `train.csv` and `test.csv` are present in the same directory as `housing_prices.py`.

**Output:**

The script will output:

*   Mean Absolute Error (MAE) on the validation set in the console.
*   A `submission.csv` file containing the predicted SalePrice for each Id in the test dataset.

## Features

-   Uses Random Forest Regressor for price prediction.
-   Performs data splitting and model evaluation.
-   Saves predictions to a CSV file for submission.
-   Trains the model using a selected set of features.

## Contributing

Feel free to fork this repository and submit pull requests to [BernardoMarta's repository](https://github.com/BernardoMarta/Housing_Prices)!

## License

This project is licensed under the MIT License.

## Acknowledgments

-   Thanks to the [Kaggle House Prices Competition](https://www.kaggle.com/c/home-data-for-ml-course/data) for providing the dataset.
-   Thanks to the `pandas`, `scikit-learn`, and `numpy` libraries for enabling key functionalities.
