import os
import subprocess
from config import ASSETS_DIR

# Get the directory where 'run_all.py' is currently located (/app)
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Point directly to main_orchestrator.py inside the /app folder
ORCHESTRATOR_PATH = os.path.join(APP_DIR, 'main_orchestrator.py')

# Create a clean copy of the environment variables
my_env = os.environ.copy()
if "GOOGLE_APPLICATION_CREDENTIALS" in my_env:
    del my_env["GOOGLE_APPLICATION_CREDENTIALS"]

# Process files
for filename in os.listdir(ASSETS_DIR):
    if filename.lower().endswith((".jpg", ".png")):
        print(f"--- Processing: {filename} ---")
        # Run using the corrected path
        subprocess.run(['python', ORCHESTRATOR_PATH, filename], env=my_env)

print("All audits complete.")