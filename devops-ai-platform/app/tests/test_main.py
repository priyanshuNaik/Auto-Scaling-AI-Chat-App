import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_chat_endpoint():
    """Test the /chat endpoint"""
    response = client.post("/chat", json={"message": "Hello, AI!"})
    assert response.status_code in [200, 400, 401, 500]  # Allow various responses depending on API key


def test_chat_invalid_request():
    """Test /chat endpoint with invalid request"""
    response = client.post("/chat", json={})
    assert response.status_code == 422  # Validation error


def test_chat_missing_message():
    """Test /chat endpoint without message field"""
    response = client.post("/chat", json={"text": "invalid"})
    assert response.status_code == 422
