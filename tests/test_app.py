import pytest
import requests

# Osnovni URL strežnika
BASE_URL = "http://localhost:5001"

# Test za končni toček /
def test_hello_world():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.text == "Hello Wor"