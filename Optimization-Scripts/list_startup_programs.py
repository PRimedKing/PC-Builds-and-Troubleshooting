"""
list_startup_programs.py
Purpose: List startup programs on Windows (read-only)
How it works:
- Queries Windows Registry for startup programs.
- Prints names and paths of startup apps.
Note: Read-only, safe to run.
"""

import winreg

def list_startup_programs():
    reg_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
    ]
    print("Startup Programs:")
    for path in reg_paths:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                name, value, _ = winreg.EnumValue(key, i)
                print(f"{name}: {value}")
        except Exception:
            continue

if __name__ == "__main__":
    list_startup_programs()
