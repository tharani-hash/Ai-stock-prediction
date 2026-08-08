import streamlit as st
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression

# Title
st.title("AI Stock Analysis Dashboard")
st.write("Analyze any company's stock using AI!")

# Get stock symbol from user
ticker = st.text_input(
    "Enter the stock symbol",
    "TCS.NS"
)

# Analyze button
if st.button("Analyze"):

    # Get stock data
    stock = yf.Ticker(ticker)
    data = stock.history(period="2y")

    # Check whether data is available
    if data.empty:
        st.error("No stock data found. Please check the stock symbol.")
        st.stop()

    # Reset index
    data = data.reset_index()

    # Price History
    
    st.subheader("📊 Price History")

    st.line_chart(
        data.set_index("Date")["Close"]
    )

    
    # Moving Averages
    data["MA7"] = data["Close"].rolling(7).mean()
    data["MA30"] = data["Close"].rolling(30).mean()

    st.subheader("📈 Trend Analysis")

    st.line_chart(
        data.set_index("Date")[["Close", "MA7", "MA30"]]
    )

    # Machine Learning Prediction
    
    data["Day_Number"] = range(len(data))

    X = data[["Day_Number"]]
    y = data["Close"]

    # Create Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X, y)

    # Predict next day's price
    next_day = [[len(data)]]
    next_price = model.predict(next_day)[0]

    
    # Display Prediction
    
    st.subheader("🔮 AI Prediction")

    st.metric(
        "Predicted Next-Day Price",
        f"₹{next_price:.2f}"
    )
