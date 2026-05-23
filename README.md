# tiny‑health‑check‑2024

A **tiny** HTTP health‑check service written in Python.

- **One endpoint**: `GET /health` → `{ "status": "ok" }`
- **Zero‑dependency runtime** – only `fastapi` & `uvicorn`
- **Built‑in CI/CD** using GitHub Actions:
  - Lint with `ruff`
  - Unit tests with `pytest`
  - Docker image build & push to GHCR on every tag

## Quick start (local)
```bash
# clone the repo
git clone https://github.com/your‑username/tiny-health-check-2024.git
cd tiny-health-check-2024

# create a venv & install deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# run the service
uvicorn app:app --host 0.0.0.0 --port 8000
```
Visit `http://localhost:8000/health` → `{"status":"ok"}`.

## Docker
```bash
# build
docker build -t ghcr.io/<owner>/tiny-health-check-2024:latest .
# run
docker run -p 8000:8000 ghcr.io/<owner>/tiny-health-check-2024:latest
```

## CI workflow
The repository ships a **GitHub Actions** workflow (`.github/workflows/ci.yml`).
- Runs on each push and pull‑request.
- On a new tag (`v*`), builds and pushes the Docker image to the GitHub Container Registry.

## License
MIT – see `LICENSE`.
