# Company Package

The **Company Package** is a Python package designed to model companies across different sectors.

## Features

- Base `Company` class with core attributes and methods, including stock price retrieval.
- Sector-specific subclasses:
  - **InfoTechCompany**: For companies focused on information technology.
  - **FinTechCompany**: For companies in the financial technology sector.
  - **MedicalCompany**: With additional methods to track drug approval attempts.
- Integrated with `yfinance` for real-time stock information.

## Installation

Ensure you have Python 3.6 or higher. You can install the package and its dependencies from source with:

```bash
pip install -e .
```

or from PyPi with:

```bash
pip install company_package
```

## Usage

Here's a quick example of how to use the package:

```python
import company as cp

my_company = cp.Company(name="Nvidia", ticker="NVDA")
my_company.display_info()

```

## Documentation

Visit our [documentation page](https://your-readthedocs-url-here).

## Contributing

Contributions are welcome! Fork our repository and submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
