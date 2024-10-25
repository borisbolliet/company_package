# src/company/company.py

import yfinance as yf
import pandas as pd

class Company:
    def __init__(self, name, ticker=None):
        """
        Initialize a Company instance.

        Parameters:
        - name (str): Name of the company.
        - ticker (str): Stock ticker symbol if the company is publicly traded.
        """
        self.name = name
        self.ticker = ticker

    def display_info(self):
        """Displays basic information about the company."""
        print(f"Company Name: {self.name}")
        if self.ticker:
            print(f"Ticker Symbol is: {self.ticker}")

    def get_yfinance_status(self):
        """
        Checks if the company stock data is available on yfinance.

        Returns:
        - str: "Available on yfinance" if the ticker has stock history data, otherwise "Not available on yfinance".
        """
        if self.ticker:
            stock = yf.Ticker(self.ticker)
            try:
                # Check if there is any historical data for the ticker
                history = stock.history(period="1d")
                if not history.empty:
                    return "Available on yfinance"
            except Exception as e:
                print(f"Error checking ticker {self.ticker}: {e}")
        
        return "Not available on yfinance"


    def get_stock_info(self, period="1y"):
        """
        Retrieves stock price history for the specified period.

        Parameters:
        - period (str): Period for which to retrieve stock history (e.g., '1y', '6mo', '1d').

        Returns:
        - history (pd.DataFrame): Stock price history.
        """
        if not self.ticker:
            print("This company is not publicly traded.")
            return None

        stock = yf.Ticker(self.ticker)
        history = stock.history(period=period)

        return history