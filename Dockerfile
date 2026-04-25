# Stage 1: Test
FROM python:3.11-slim AS test
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt pytest-cov
COPY app/ .
ENV PYTHONPATH=/app
RUN pytest tests/ -v --cov=. --cov-report=xml --cov-report=term

# Stage 2: Build
FROM python:3.11-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
COPY --from=test /app/coverage.xml .
EXPOSE 8000
CMD ['uvicorn', 'main:app', '--host', '0.0.0.0', '--port', '8000']
