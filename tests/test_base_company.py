# tests/test_base_company.py

import pytest
from company.base_company import Company

def test_init():
    company = Company(name="Test Corp", ticker="TST")
    assert company.name == "Test Corp"
    assert company.ticker == "TST"

def test_display_info(capsys):
    company = Company(name="Test Corp", ticker="TST")
    company.display_info()
    captured = capsys.readouterr()
    assert "Company Name: Test Corp" in captured.out
    assert "Ticker Symbol is: TST" in captured.out

def test_get_yfinance_status():
    company = Company(name="Test Corp", ticker="AAPL")  # Use a known ticker
    result = company.get_yfinance_status()
    assert result == "Available on yfinance" or result == "Not available on yfinance"  # Avoiding hardcoding

def test_get_stock_info():
    company = Company(name="Test Corp", ticker="AAPL")
    history = company.get_stock_info("1d")
    assert history is not None
    assert not history.empty
