FROM python:3.12-slim@sha256:8d7f5c9b10c983dbf9d7fe0c89e6131a6a8c0cb5c0e6920c058695c9f9d2685e

# Install runtime deps only (no build‑tools)
RUN pip install --no-cache-dir \
    fastapi==0.112.0 \
    uvicorn[standard]==0.30.1

WORKDIR /app
COPY app.py ./

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
