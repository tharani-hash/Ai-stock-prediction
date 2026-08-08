import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


# PAGE CONFIGURATION
st.set_page_config(
    page_title="AI Stock Analysis Dashboard",
    page_icon="📈",
    layout="wide"
)
# TITLE
st.title("📈 AI Stock Analysis Dashboard")
st.write(
    "Analyze stock price history, trends, and make a simple "
    "machine-learning prediction."
)

# USER INPUT
ticker = st.text_input(
    "Enter Stock Symbol",
    "TCS.NS"
)
analyze = st.button("🔍 Analyze Stock")

# MAIN ANALYSIS

if analyze:

    # 1. GET STOCK DATA

    st.subheader("📥 Downloading Stock Data...")

    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="2y")

    except Exception as e:
        st.error(f"Unable to download stock data: {e}")
        st.stop()


    # Check whether data was received

    if data.empty:
        st.error(
            "No stock data found. Please check the stock symbol."
        )
        st.stop()


    # Reset index

    data = data.reset_index()


    st.success(
        f"Successfully downloaded {len(data)} trading days of data."
    )


    # 2. DISPLAY RAW DATA
    st.subheader("📊 Historical Stock Data")

    st.dataframe(
        data.tail(20),
        use_container_width=True
    )

    # 3. PRICE HISTORY
    st.subheader("📈 Stock Price History")

    st.line_chart(
        data.set_index("Date")["Close"]
    )

    # 4. MOVING AVERAGES
    # Calculate 7-day moving average
    data["MA7"] = (
        data["Close"]
        .rolling(window=7)
        .mean()
    )


    # Calculate 30-day moving average

    data["MA30"] = (
        data["Close"]
        .rolling(window=30)
        .mean()
    )
    st.subheader(
        "📊 Trend Analysis: 7-Day vs 30-Day Moving Average"
    )


    st.line_chart(
        data.set_index("Date")[
            ["Close", "MA7", "MA30"]
        ]
    )

    # 5. PREPARE DATA FOR MACHINE LEARNING
    # Machine-learning models work with numbers,
    # so convert each trading day into a sequential number.

    data["Day_Number"] = range(len(data))
    # X = input feature
    X = data[["Day_Number"]]
    # y = target value
    y = data["Close"]
    # 6. SPLIT DATA INTO TRAINING AND TESTING

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        shuffle=False
    )

    # 7. CREATE AND TRAIN MODEL
    model = LinearRegression()
    model.fit(
        X_train,
        y_train
    )

    # 8. TEST THE MODEL
    predictions = model.predict(
        X_test
    )
    # Calculate Mean Absolute Error

    error = mean_absolute_error(
        y_test,
        predictions
    )

    # 9. MODEL PERFORMANCE
    st.subheader(" Machine Learning Model Performance")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Average Prediction Error",
            f"₹{error:.2f}"
        )

    with col2:
        st.metric(
            "Training Data",
            f"{len(X_train)} days"
        )


    # 10. ACTUAL VS PREDICTED PRICE
    st.subheader(
        "📉 Actual vs Predicted Prices"
    )
    prediction_data = pd.DataFrame(
        {
            "Actual Price": y_test.values,
            "Predicted Price": predictions
        },
        index=data.loc[
            X_test.index,
            "Date"
        ]
    )


    st.line_chart(
        prediction_data
    )

    # 11. NEXT-DAY PREDICTION
    next_day = [[len(data)]]
    next_price = model.predict(
        next_day
    )[0]


    # 12. DISPLAY PREDICTION

    st.subheader(" AI Stock Price Prediction")
    st.metric(
        "Predicted Next-Day Price",
        f"₹{next_price:.2f}"
    )

    # 13. CURRENT PRICE


    current_price = data["Close"].iloc[-1]


    st.metric(
        "Latest Closing Price",
        f"₹{current_price:.2f}"
    )

    # 14. PRICE DIFFERENCE
    difference = next_price - current_price
    percentage_change = (
        difference / current_price
    ) * 100
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Price Difference",
            f"₹{difference:.2f}"
        )

    with col2:
        st.metric(
            "Predicted Percentage Change",
            f"{percentage_change:.2f}%"
        )

    # 15. DOWNLOAD DATA
    st.subheader(" Download Stock Data")


    csv_data = data.to_csv(
        index=False
    )
    st.download_button(
        label="📥 Download CSV",
        data=csv_data,
        file_name=f"{ticker}_stock_data.csv",
        mime="text/csv"
    )
    
