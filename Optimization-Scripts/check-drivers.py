"""
check_drivers.py
Purpose: Check GPU and OS driver versions (read-only)
How it works:
- Uses subprocess to get GPU info via 'wmic' on Windows.
- Prints current OS version and driver info.
Note: Does not perform updates; safe to run.
"""

import platform
import subprocess

def check_drivers():
    print("OS Version:", platform.platform())
    try:
        gpu_info = subprocess.check_output(
            'wmic path win32_VideoController get name, driverversion', shell=True
        ).decode()
        print("GPU Info:\n", gpu_info)
    except Exception as e:
        print("Error retrieving GPU info:", e)

if __name__ == "__main__":
    check_drivers()
