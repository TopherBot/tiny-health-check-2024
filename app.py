from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="tiny‑health‑check‑2024")

@app.get("/health", response_class=JSONResponse)
def health() -> dict:
    """Return a tiny JSON health payload.
    
    This endpoint can be used by load‑balancers, Kubernetes liveness/readiness
    probes, or any monitoring system.
    """
    return {"status": "ok"}

if __name__ == "__main__":
    # When run directly (e.g. `python app.py`) start a dev server.
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
