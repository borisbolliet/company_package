import pytest
from company.cli import main

def test_display_info(capsys, monkeypatch):
    # Mock command-line arguments
    monkeypatch.setattr("sys.argv", ["cli.py", "display_info", "--ticker", "AAPL"])
    
    # Run the CLI main function
    main()
    
    # Capture output
    captured = capsys.readouterr()

    print(captured.out)
    
    # Check that output contains expected text (example output)
    assert "Company Name: N/A" in captured.out
    assert "Ticker Symbol is: AAPL" in captured.out


def test_get_stock_price_difference(capsys, monkeypatch):
    # Mock command-line arguments with a known ticker and date range
    monkeypatch.setattr("sys.argv", [
        "cli.py", "get_stock_price_difference", 
        "--ticker", "AAPL", 
        "--interval", "1y", 
        "--stop_date", "2023-12-31"
    ])
    
    # Run the CLI main function
    main()
    
    # Capture output
    captured = capsys.readouterr()

    # # Test the numeric value directly by extracting it from the output
    price_diff = float(captured.out.split(": ")[1].strip())
    # assert abs(price_diff - 18.717864990234) < 1e-4


    # Test using pytest.approx for better floating point comparison
    assert price_diff == pytest.approx(18.717864990234, rel=1e-4)

    
    


