FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Default: run the rule-based agent demo
# Override with: docker run ... python -m uvicorn server.app:app --host 0.0.0.0 --port 8000
CMD ["python", "inference.py"]
