import os

# Get the directory where 'app' is located, then go up one level to the root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Add your CSV filename here
FSSAI_CSV = os.path.join(DATA_DIR, "FSSAI_Compliance_Validation_Rules_V2.xlsx")