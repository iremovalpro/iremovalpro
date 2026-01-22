# License and trial management
# Stores trial usage locally for demonstration purposes

import json
import os
from config import MAX_TRIALS

LICENSE_FILE = "license.json"

def load_license():
    if not os.path.exists(LICENSE_FILE):
        return {"trials_left": MAX_TRIALS}
    with open(LICENSE_FILE, "r") as f:
        return json.load(f)

def save_license(data):
    with open(LICENSE_FILE, "w") as f:
        json.dump(data, f)

def use_trial():
    data = load_license()
    if data["trials_left"] <= 0:
        return False
    data["trials_left"] -= 1
    save_license(data)
    return True

def trials_left():
    return load_license()["trials_left"]
