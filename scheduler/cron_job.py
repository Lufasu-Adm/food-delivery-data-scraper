import time
import schedule
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import run_pipeline

def job():
    print(f"\n[Scheduler] Running automated pipeline at: {time.ctime()}")
    run_pipeline()

# Menjalankan script setiap 1 jam
schedule.every(1).hours.do(job)

if __name__ == "__main__":
    print("Scheduler activated. Pipeline will run every 1 hour.")
    print("Press Ctrl+C to terminate.")

    while True:
        schedule.run_pending()
        time.sleep(1)