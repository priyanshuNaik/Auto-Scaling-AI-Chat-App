# Stage 1: Test
FROM python:3.11-slim AS test
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
RUN pytest tests/ -v


# Stage 2: Build
FROM python:3.11-slim AS build
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
EXPOSE 8000
CMD ['uvicorn', 'main:app', '--host', '0.0.0.0', '--port', '8000']
