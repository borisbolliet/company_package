# tests/test_medical_company.py

import pytest
from company.medical.medical import MedicalCompany
import pandas as pd

def test_medical_init():
    med_company = MedicalCompany(name="MediCorp", specialty="Cardiology", drug_manufacturer=True)
    assert med_company.name == "MediCorp"
    assert med_company.specialty == "Cardiology"
    assert med_company.drug_manufacturer is True

def test_drug_approval_summary(monkeypatch, capsys):
    data = pd.DataFrame({
        "company_name": ["MediCorp", "OtherCorp"],
        "drug_name": ["Drug A", "Drug B"],
        "approval_attempts": [3, 1]
    })
    
    def mock_read_csv(*args, **kwargs):
        return data

    # Replace pd.read_csv with mock_read_csv for the test
    # monkeypatch is a pytest feature 
    monkeypatch.setattr(pd, "read_csv", mock_read_csv)

    med_company = MedicalCompany(name="MediCorp", specialty="Cardiology", drug_manufacturer=True)
    med_company.drug_approval_summary()

    # the method above prints into stdout
    # we need to capture this output
    # we do that with capsys, another pytest feature

    captured = capsys.readouterr()
    
    assert "Drug Approval Summary for MediCorp:" in captured.out
    assert "Drug A: 2 failed attempt(s) before approval" in captured.out
