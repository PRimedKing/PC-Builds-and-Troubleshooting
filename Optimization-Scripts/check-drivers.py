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
import webbrowser

def check_drivers():
    print("OS Version:", platform.platform())
    
    try:
        gpu_info = subprocess.check_output(
            'wmic path win32_VideoController get name, driverversion', shell=True
        ).decode()
        print("GPU Info:\n", gpu_info)
        
        print("Check latest driver version online:")
        # Example: NVIDIA link
        webbrowser.open("https://www.nvidia.com/Download/index.aspx")
        # For AMD, you can replace the link with https://www.amd.com/en/support
    except Exception as e:
        print("Error retrieving GPU info:", e)

if __name__ == "__main__":
    check_drivers()
