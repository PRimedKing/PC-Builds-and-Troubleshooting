"""
monitor_system.py
Purpose: Monitor CPU, RAM, and Disk usage in real-time.
How it works:
- Uses psutil to get system metrics.
- Prints CPU usage %, memory usage %, and disk usage %.
"""

import psutil

def system_monitor():
    print("CPU Usage: ", psutil.cpu_percent(), "%")
    print("Memory Usage: ", psutil.virtual_memory().percent, "%")
    print("Disk Usage: ", psutil.disk_usage('/').percent, "%")

if __name__ == "__main__":
    system_monitor()
