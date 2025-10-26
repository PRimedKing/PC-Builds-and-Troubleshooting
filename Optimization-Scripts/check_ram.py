"""
check_ram.py
Purpose: Detect RAM speed and XMP profile (read-only).
How it works:
- Uses 'psutil' and 'subprocess' to get RAM information.
- Prints total RAM, current speed, and XMP profile info if available.
Note: Cannot change XMP; this is safe and read-only.
"""

import psutil
import platform
import subprocess

def check_ram():
    print(f"Total RAM: {round(psutil.virtual_memory().total / (1024**3))} GB")
    
    if platform.system() == "Windows":
        try:
            output = subprocess.check_output(
                'wmic memorychip get speed, partnumber, capacity', shell=True
            ).decode()
            print("RAM Details:\n", output)
            print("If your RAM supports XMP, enable it in BIOS for optimal speed.")
        except Exception as e:
            print("Error retrieving RAM info:", e)
    else:
        print("Detailed RAM speed info may require admin privileges on Linux/Mac.")

if __name__ == "__main__":
    check_ram()
