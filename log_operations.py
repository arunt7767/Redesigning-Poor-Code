from datetime import datetime
import os

LOG_FILE = "data/operations.log"

def ensure_log_dir():
    log_dir = os.path.dirname(LOG_FILE)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

def log_operation(message):
    """Logs operations to a file."""
    ensure_log_dir()
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")

def list_log_entries():
    ensure_log_dir()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as log_file:
            log_entries = log_file.readlines()
            if log_entries:
                for entry in log_entries:
                    print(entry.strip())
            else:
                print("No log entries found.")
    else:
        print("Log file does not exist.")
