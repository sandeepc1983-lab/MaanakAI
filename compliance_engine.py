import re
import pandas as pd
import os
from config import FSSAI_CSV

class ComplianceEngine:
    def __init__(self):
        # Update path to look for .xlsx based on the filename in image_ac50cd.png
        excel_path = FSSAI_CSV.replace('.csv', '.xlsx')
        
        if os.path.exists(excel_path):
            # Load using openpyxl engine
            self.rules_df = pd.read_excel(excel_path, engine='openpyxl')
            print(f"Success: Rules loaded from {excel_path}")
        else:
            print(f"Error: Could not find file at {excel_path}")
            self.rules_df = None

    def validate(self, text):
        patterns = {
            'product_name': r'(?i)(Himalayan\s*Brew|Berry\s*Biscus|Smarat|Hide\s*and\s*Stick)',
            'batch_number': r'(?i)(?:batch|lot|b\.?|no\.?|batchno)[^\w]*([A-Z0-9a-z]{3,15})',
            'best_before': r'(?i)(?:best\s*before|expiry|exp|use\s*by)[^\w]*([\d\./\-]{5,})',
            'fssai_license': r'(\d{14})'
        }
        
        results = {}
        extracted = {}
        
        for key, pattern in patterns.items():
            match = re.search(pattern, text)
            # Safely get match group
            if match:
                extracted[key] = match.group(1).strip() if match.groups() else match.group(0).strip()
                results[key] = "PASS"
            else:
                extracted[key] = "Not Detected"
                results[key] = "FAIL"
                
        return results, extracted