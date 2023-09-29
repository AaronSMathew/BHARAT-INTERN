# BHARAT-INTERN


# Repository Name: Machine Learning Projects

## Overview

This repository contains two distinct machine learning projects that demonstrate practical applications of data analysis, modeling, and user interface development using Python libraries. Below, we'll provide an overview of each project along with instructions on how to run them.

## Project 1: Stock Price Prediction

### Description

Project 1 focuses on predicting stock prices using a Long Short-Term Memory (LSTM) neural network. It involves data preprocessing, model building, training, and visualization of the prediction results.

### Usage

1. **Data Preparation**: Replace `'stock.csv'` with your own dataset containing stock price data. Make sure the CSV file has a 'Close' column, which is assumed to contain the stock prices.

2. **Normalization**: The data is normalized using Min-Max scaling to bring all values within the range [0, 1].

3. **Data Sequencing**: The data is sequenced to create input-output pairs for training the LSTM model. The sequence length can be adjusted by modifying the `seq_length` variable.

4. **Train-Test Split**: The dataset is split into training and testing sets (80% for training, 20% for testing).

5. **LSTM Model**: An LSTM neural network is defined using PyTorch. You can modify the hyperparameters like `hidden_size`, `num_layers`, and `num_epochs` based on your requirements.

6. **Training**: The model is trained using the training data, and the loss is displayed at regular intervals.

7. **Testing and Visualization**: The trained model is used to make predictions on the test data. Predictions and true values are denormalized and visualized using matplotlib.

### Dependencies

- pandas
- numpy
- torch
- matplotlib
- sklearn

## Project 2: Titanic Survival Predictor

### Description

Project 2 involves building a graphical user interface (GUI) application for predicting whether a passenger on the Titanic survived or not. It uses a Random Forest classifier to make predictions based on passenger information.

### Usage

1. **Dataset**: The Titanic dataset is loaded from seaborn and saved as 'titanic.csv'. You can replace it with your own dataset or use different features.

2. **Data Preprocessing**: Features like 'sex' are mapped to numeric values, missing values in 'age' are filled with the median, and only selected columns are retained.

3. **Classifier Training**: A Random Forest classifier is trained on the preprocessed data. You can experiment with different classifiers and hyperparameters.

4. **GUI Application**: The tkinter library is used to create a GUI application for predicting survival. The user inputs passenger information, and the application displays the prediction result.

### Dependencies

- tkinter
- seaborn
- numpy
- pandas
- scikit-learn

## How to Run

1. Clone the repository to your local machine.

2. Install the required dependencies using `pip install -r requirements.txt`.

3. Run the respective Python scripts for each project:

   - For Project 1 (Stock Price Prediction): `python stock_price_prediction.py`
   - For Project 2 (Titanic Survival Predictor): `python titanic_survival_predictor.py`

Follow the on-screen instructions for each project to interact with and explore the functionalities.

## Contribution

Feel free to contribute to this repository by improving existing projects, adding new projects, or suggesting enhancements. Fork the repository, make your changes, and create a pull request.

We welcome your feedback and contributions to make these projects even better!

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more details.

---

Please note that this README is a general template and may need specific adjustments depending on the actual content, structure, and requirements of your repository.
