from fastapi import FastAPI
import socket
import time

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/process")
def heavy_process():
    start = time.time()
    
    total = 0
    for i in range(30000):
        for j in range(3000):
            total += (i * j) % 7

    elapsed = time.time() - start
    hostname = socket.gethostname()

    return {
        "result": total,
        "processing_time": elapsed,
        "machine": hostname
    }
