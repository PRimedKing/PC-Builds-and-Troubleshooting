"""
backup_files.py
Purpose: Automates backup of important files.
How it works:
- Copies files from 'important_files' folder to 'backups' with timestamp.
- Creates 'backups' folder if missing.
"""

import shutil
import os
from datetime import datetime

def backup_files():
    source_folder = "./important_files"
    backup_folder = "./backups"
    os.makedirs(backup_folder, exist_ok=True)
    
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_folder, f"backup_{date_str}")
    
    if os.path.exists(source_folder):
        shutil.copytree(source_folder, backup_path)
        print(f"Files backed up to {backup_path}")
        print(f"Backup folder size: {round(sum(os.path.getsize(os.path.join(dirpath, f)) for dirpath, _, files in os.walk(backup_path) for f in files)/1024/1024, 2)} MB")
    else:
        print(f"Source folder '{source_folder}' not found.")

if __name__ == "__main__":
    backup_files()
