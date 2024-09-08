import requests

BASE_URL = "https://petstore.swagger.io/v2"

def add_pet(pet_id, pet_name, pet_status, photo_url):
    """Helper function to add a pet."""
    url = f"{BASE_URL}/pet"
    payload = {
      "id": pet_id,
      "name": pet_name,
      "photoUrls": photo_url,
      "status": pet_status
    }
    response = requests.post(url, json=payload)
    return response, pet_id

def update_pet(pet_id, name, status):
    """Helper function to update a pet using form data."""
    url = f"{BASE_URL}/pet/{pet_id}"
    data = {
        'name': name,
        'status': status
    }
    response = requests.post(url, data=data)
    return response

def delete_pet(pet_id, api_key):
    """Helper function to delete a pet using API key."""
    url = f"{BASE_URL}/pet/{pet_id}"
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.delete(url, headers=headers)
    return response

def upload_image(pet_id, file_path, additional_metadata=None):
    """Helper function to upload an image for a pet."""
    url = f"{BASE_URL}/pet/{pet_id}/uploadImage"
    files = {'file': open(file_path, 'rb')}
    params = {'additionalMetadata': additional_metadata} if additional_metadata else {}
    response = requests.post(url, files=files, params=params)
    return response

