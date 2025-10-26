"""
monitor_system.py
Purpose: Monitor CPU, RAM, and Disk usage in real-time.
How it works:
- Uses psutil to get system metrics.
- Prints CPU usage %, memory usage %, and disk usage %.
"""

import psutil

def system_monitor():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    print("CPU Usage: ", cpu, "%")
    print("Memory Usage: ", ram, "%")
    print("Disk Usage: ", disk, "%")
    
    if cpu > 85:
        print("Warning: High CPU usage!")
    if ram > 85:
        print("Warning: High RAM usage!")
    if disk > 90:
        print("Warning: Low disk space!")

if __name__ == "__main__":
    system_monitor()
