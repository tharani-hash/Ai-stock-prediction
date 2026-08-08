# AI Stock Analysis Dashboard

An interactive stock analysis and machine learning application built with Python and Streamlit. The application retrieves historical stock market data, performs basic technical analysis, evaluates a machine learning model, and generates a next-day stock price prediction.

## Overview

The AI Stock Analysis Dashboard provides an end-to-end demonstration of a basic machine learning workflow applied to financial market data.

Users can enter a stock symbol, retrieve historical data from Yahoo Finance, analyze price trends using moving averages, evaluate a Linear Regression model, and view an estimated next-day closing price.

The project is designed as an educational and portfolio project demonstrating data acquisition, data preprocessing, exploratory analysis, machine learning, model evaluation, and application deployment.

## Features

### Historical Stock Data

* Retrieves approximately two years of historical stock data.
* Supports stock symbols available through Yahoo Finance.
* Displays recent historical data within the application.
* Provides an option to download the processed data as a CSV file.

### Price Analysis

The application provides historical closing price visualization to help users understand the overall price movement of a selected stock.

### Moving Average Analysis

Two moving averages are calculated:

* 7-day moving average for short-term trend analysis.
* 30-day moving average for longer-term trend analysis.

The actual closing price and moving averages are displayed together to provide a simple view of price trends.

### Machine Learning

The current implementation uses Linear Regression to demonstrate basic stock price prediction.

The workflow includes:

1. Converting trading dates into sequential numerical values.
2. Defining the day number as the input feature.
3. Using the closing price as the target variable.
4. Splitting the historical data into training and testing datasets.
5. Training a Linear Regression model.
6. Generating predictions on the test dataset.
7. Evaluating model performance using Mean Absolute Error.
8. Generating an estimated next-day closing price.

### Model Evaluation

The model is evaluated using Mean Absolute Error (MAE).

The application also provides a comparison between actual and predicted prices for the test dataset.

## Technology Stack

| Technology   | Purpose                                      |
| ------------ | -------------------------------------------- |
| Python       | Application and machine learning development |
| Streamlit    | Interactive web application                  |
| yfinance     | Historical stock market data                 |
| Pandas       | Data processing and manipulation             |
| Matplotlib   | Data visualization                           |
| Scikit-learn | Machine learning and model evaluation        |

## Project Structure

```text
AI-Stock-Analysis/
│
├── app.py
├── requirements.txt
└── README.md
```

The project intentionally uses a single application file for the current version. The complete workflow, including data retrieval, analysis, visualization, machine learning, evaluation, and prediction, is implemented in `app.py`.

## Application Workflow

```text
User Input
    |
    v
Stock Symbol
    |
    v
Yahoo Finance
    |
    v
Historical Stock Data
    |
    v
Data Processing
    |
    +----------------------+
    |                      |
    v                      v
Price Analysis       Moving Averages
    |                      |
    +----------+-----------+
               |
               v
       Machine Learning
               |
               v
       Linear Regression
               |
        +------+------+
        |             |
        v             v
 Model Evaluation   Prediction
        |             |
        +------+------+
               |
               v
        Streamlit Dashboard
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Stock-Analysis.git
```

Navigate to the project directory:

```bash
cd AI-Stock-Analysis
```

### 2. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the dependencies manually:

```bash
pip install streamlit yfinance pandas matplotlib scikit-learn
```

## Requirements

The `requirements.txt` file should contain:

```text
streamlit
yfinance
pandas
matplotlib
scikit-learn
```

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

After starting the application, Streamlit will provide a local URL that can be opened in a web browser.

## Usage

1. Open the application.
2. Enter a valid stock symbol.
3. Click the Analyze Stock button.
4. Review the historical stock data.
5. Analyze the closing price trend.
6. Review the 7-day and 30-day moving averages.
7. Review the machine learning model performance.
8. Compare actual and predicted prices.
9. View the estimated next-day stock price.
10. Download the processed stock data if required.

### Example Stock Symbols

For Indian stocks listed on the National Stock Exchange, examples include:

```text
TCS.NS
INFY.NS
RELIANCE.NS
HDFCBANK.NS
ICICIBANK.NS
SBIN.NS
ITC.NS
WIPRO.NS
```

## Machine Learning Methodology

The current version uses a simple Linear Regression model.

The input feature is:

```text
Day Number
```

The target variable is:

```text
Closing Price
```

The dataset is divided chronologically into:

```text
80% Training Data
20% Testing Data
```

The test data is not randomly shuffled because the project works with time-dependent financial observations.

Model performance is measured using Mean Absolute Error.

## Limitations

This project should be considered a basic machine learning demonstration rather than a production-grade financial forecasting system.

The current model has several limitations:

* It uses only the sequential day number as the primary predictive feature.
* It does not incorporate trading volume.
* It does not use technical indicators such as RSI or MACD.
* It does not consider market or sector performance.
* It does not incorporate company financial fundamentals.
* It does not consider financial news or market sentiment.
* It does not model complex time-series relationships.
* It does not provide prediction uncertainty or confidence intervals.
* Historical performance does not guarantee future results.

Because of these limitations, the generated prediction should not be used as a standalone investment decision.

## Future Improvements

The project can be extended into a more robust financial machine learning system by introducing additional features and more appropriate time-series methodologies.

### Feature Engineering

Potential features include:

* Lagged closing prices
* Daily returns
* Trading volume
* Rolling volatility
* RSI
* MACD
* Bollinger Bands
* Moving average ratios
* Market index returns
* Sector-level indicators

### Machine Learning Models

Future versions can evaluate and compare multiple models, including:

* Linear Regression
* Random Forest
* Gradient Boosting
* XGBoost
* LightGBM
* Support Vector Regression

### Time-Series Models

Additional forecasting approaches can include:

* ARIMA
* SARIMA
* Prophet
* LSTM
* GRU
* Transformer-based time-series models

# Model Validation

A stronger evaluation framework can use:

* Walk-forward validation
* Expanding-window validation
* Time-series cross-validation
* Multiple evaluation metrics

#Application Improvements

Future versions can include:

* Interactive candlestick charts
* Technical indicator dashboards
* Multiple-stock comparison
* Portfolio analysis
* Risk metrics
* Model comparison
* Automated model selection
* Prediction intervals
* Market index comparison
* News sentiment analysis

#Data Source

Historical stock market data is retrieved using the `yfinance` library from Yahoo Finance.

The application retrieves data dynamically when an analysis is performed.

Data Science and Machine Learning Project

# License

This project is intended for educational and portfolio use.
