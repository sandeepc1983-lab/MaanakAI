import gspread
from google.auth import default
import traceback

def get_fssai_rules():
    print("Attempting to get default credentials...")
    creds, _ = default(scopes=[
        'https://www.googleapis.com/auth/spreadsheets.readonly',
        'https://www.googleapis.com/auth/drive.readonly'
    ])
    print(f"Credentials acquired: {creds}")
    
    gc = gspread.authorize(creds)
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1ATD1x0crAojQKMWCECd7jtoqSZGBAAGY2pq4x7Zpbk0/edit"
    
    print("Opening spreadsheet by URL...")
    sh = gc.open_by_url(spreadsheet_url)
    return sh.sheet1.get_all_records()

if __name__ == "__main__":
    try:
        data = get_fssai_rules()
        print("Successfully connected!")
    except Exception:
        print("--- DETAILED ERROR TRACEBACK ---")
        traceback.print_exc()