# company/__init__.py

# Import the main Company class for easy access
from .base_company import Company

# Import specific submodule classes
from .medical.medical import MedicalCompany

# Import version information for the package
from .version import __version__  # Ensure version.py contains this variable

# Print the package version for confirmation (optional)
print(f"Company package version: {__version__}")

