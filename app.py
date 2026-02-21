import threading
import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"ok": True}

def run_agent():
    # Temporary placeholder
    while True:
        time.sleep(60)

@app.on_event("startup")
def startup():
    threading.Thread(target=run_agent, daemon=True).start()
