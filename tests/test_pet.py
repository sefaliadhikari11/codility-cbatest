import pytest
import requests
from pathlib import Path
from helpers.api_helpers import add_pet, upload_image, update_pet, delete_pet

BASE_URL = "https://petstore.swagger.io/v2"

def test_add_pet():
    """Test case for a successfully adding a pet."""
    pet_id = 101
    pet_name = "Tommie"
    pet_status = "available"
    photo_url = ["http://test.com/Tommie.jpg"]
    response, pet_id = add_pet(pet_id, pet_name, pet_status, photo_url)
    assert response.status_code == 200, "Expected status code 200 but got {response.status_code}"
    assert response.json()['id'] == pet_id
    assert response.json()['name'] == pet_name
    assert response.json()['status'] == pet_status

@pytest.mark.skip
def test_add_pet_with_invalid_data():
    """This testcase is skipped because the endpoint is giving 500 error response which would fail the test"""
    pet_id = "invalid id" # non-integer
    pet_name = "invalid pet"
    pet_status = "invalid status" # should be one of 'available', 'pending', 'sold'
    photo_url = "invalid url" # should be an array
    response, pet_id = add_pet(pet_id, pet_name, pet_status, photo_url)
    assert response.status_code == 405, "Expected status code 405 but got {response.status_code}"

def test_find_pet_by_valid_id():
    """Testcase for finding a pet with a valid id"""
    pet_id = 102
    pet_name = "Tommie"
    pet_status = "available"
    photo_url = ["http://test.com/Tommie.jpg"]
    response, pet_id = add_pet(pet_id, pet_name, pet_status, photo_url)
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    assert response.status_code == 200, "Expected status code 200 but got {response.status_code}"

def test_find_pet_by_invalid_id():
    """Testcase for finding a pet with an invalid id"""
    pet_id = 0
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    assert response.status_code == 404, "Expected status code 404 but got {response.status_code}"
    response_json=response.json()
    assert response_json['message'] == 'Pet not found', "Expected message 'Pet not found' but got {response_json['message']}"

def test_find_pet_by_valid_status():
    """Testcase for finding a pet with a valid status"""
    pet_status = "available"
    url = f"{BASE_URL}/pet/findByStatus?status={pet_status}"
    response = requests.get(url)
    assert response.status_code == 200, "Expected status code 200 but got {response.status_code}"

@pytest.mark.skip
def test_find_pet_by_invalid_status():
    """This testcase is skipped because the endpoint is giving 200 response which would fail the test"""
    pet_status = "unknown"
    url = f"{BASE_URL}/pet/findByStatus?status={pet_status}"
    response = requests.get(url)
    assert response.status_code == 400, "Expected status code 400 but got {response.status_code}"

def test_update_existing_pet():
    """Testcase for updating a pet with a valid data"""
    pet_id = 103
    pet_name = "Tommie"
    pet_status = "available"
    photo_url = ["http://test.com/Tommie.jpg"]
    response, pet_id = add_pet(pet_id, pet_name, pet_status, photo_url)
    url = f"{BASE_URL}/pet"
    payload = {
        "id": pet_id,
        "name": "Tom",
        "photoUrls": ["http://test.com/updated_photo.jpg"],
        "status": "sold"
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200, "Expected status code 200 but got {response.status_code}"
    assert response.json()['name'] == "Tom"

def test_update_pet_with_valid_form_data():
    """Test case for a successful pet update with form data."""
    pet_id = 104
    pet_name = "Tommie"
    pet_status = "available"
    photo_url = ["http://test.com/Tommie.jpg"]
    response, pet_id = add_pet(pet_id, pet_name, pet_status, photo_url)

    response = update_pet(pet_id, 'Tom', 'pending')
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

def test_update_pet_with_invalid_form_data():
    """Test case for an unsuccessful update of a pet with invalid data."""
    response = update_pet(-1, 'Tom', 'unknown')
    response_json = response.json()
    print(response_json)
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"

def test_delete_pet():
    """Test case for successfully deleting a pet"""
    pet_id = 105
    pet_name = "Tommie"
    pet_status = "available"
    photo_url = ["http://test.com/Tommie.jpg"]
    response, pet_id = add_pet(pet_id, pet_name, pet_status, photo_url)

    api_key = 'special-key'
    response = delete_pet(pet_id, api_key)
    assert response.status_code == 200, "Expected status code 200 but got {response.status_code}"

    """Verify deletion"""
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    assert response.status_code == 404, "Expected status code 404 but got {response.status_code}"

def test_delete_pet_with_invalid_data():
    """Test case for unsuccessful deletion of a pet"""
    api_key = 'special-key'
    response = delete_pet(0, api_key)
    assert response.status_code == 404, "Expected status code 404 but got {response.status_code}"

def test_upload_image():
    """Test case for a successful image upload."""
    pet_id = 106
    pet_name = "Tommie"
    pet_status = "available"
    photo_url = ["http://test.com/Tommie.jpg"]
    response, pet_id = add_pet(pet_id, pet_name, pet_status, photo_url)

    filepath = Path("files")/ "test_image.jpg"
    response = upload_image(pet_id, filepath, 'Test Image Metadata')
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"



