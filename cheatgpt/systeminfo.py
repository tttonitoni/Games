import psutil
import csv
import time
from datetime import datetime
import os

# Dateipfad für die CSV-Datei
FILE_PATH = 'system_metrics.csv'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Erstellen der CSV-Datei und Überschriften, falls Datei noch nicht existiert
def initialize_csv():
    with open(FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)"])

# Funktion zum Erfassen der Systemmetriken
def log_system_metrics():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    with open(FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, cpu_usage, memory_usage, disk_usage])

    print(f"{timestamp} | CPU: {cpu_usage}% | Memory: {memory_usage}% | Disk: {disk_usage}%")

# Scheduler zum Ausführen der Metrik-Erfassung alle x Sekunden
def start_logging(interval=10):
    print("System metrics logging started...")
    initialize_csv()  # CSV-Datei initialisieren
    while True:
        log_system_metrics()

# Startet das Logging mit einem Intervall von 10 Sekunden
if __name__ == "__main__":
    start_logging()
