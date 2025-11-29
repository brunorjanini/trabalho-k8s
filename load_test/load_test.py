import requests
import concurrent.futures
import csv
import time

URL = "http://20.69.18.162:8000/process"

NUM_REQUESTS = 100
MAX_WORKERS = 20

def make_request(_):
    try:
        start = time.time()
        r = requests.get(URL, timeout=30)
        elapsed = time.time() - start
        return {
            "status": r.status_code,
            "processing_time": r.json().get("processing_time"),
            "total_time": elapsed,
            "machine": r.json().get("machine")
        }
    except Exception as e:
        return {"error": str(e)}

results = []

with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    for r in executor.map(make_request, range(NUM_REQUESTS)):
        results.append(r)

with open("results.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print("Finished! Results saved in results.csv.")
