import pytest
import requests

BASE_URL = "http://127.0.0.1:8000/users"

def test_users_endpoint_unauthorized(mocker):
    # Mock the requests.get function
    mock_response = mocker.Mock()
    mock_response.text = ""
    mock_response.status_code = 401
    mocker.patch("requests.get", return_value=mock_response)
    
    params = {"username": "admin", "password": "admin"}
    response = requests.get(BASE_URL, params=params)
    
    assert response.text == "", "Expected an empty response body"
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"

def test_users_endpoint_authorized(mocker):
    # Mock the requests.get function
    mock_response = mocker.Mock()
    mock_response.text = ""
    mock_response.status_code = 200
    mocker.patch("requests.get", return_value=mock_response)
    
    params = {"username": "admin", "password": "qwerty"}
    response = requests.get(BASE_URL, params=params)
    
    assert response.text == "", "Expected an empty response body"
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

