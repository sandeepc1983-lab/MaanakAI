import os
import subprocess
from config import ASSETS_DIR

# 1. Get the directory where 'run_all.py' is located (which is /app)
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Point directly to main_orchestrator.py in the same folder
ORCHESTRATOR_PATH = os.path.join(APP_DIR, 'main_orchestrator.py')

# 3. Setup environment
my_env = os.environ.copy()
if "GOOGLE_APPLICATION_CREDENTIALS" in my_env:
    del my_env["GOOGLE_APPLICATION_CREDENTIALS"]

# 4. Process files
print(f"Scanning assets in: {ASSETS_DIR}")
for filename in os.listdir(ASSETS_DIR):
    if filename.lower().endswith((".jpg", ".png")):
        print(f"--- Processing: {filename} ---")
        # Run orchestrator
        subprocess.run(['python', ORCHESTRATOR_PATH, filename], env=my_env)

print("All audits complete.")