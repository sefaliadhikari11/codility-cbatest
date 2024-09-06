import requests
from config import BASE_URL

def test_find_pet_by_id():
    url = f"{BASE_URL}/9845"
    response = requests.get(url)

    assert response.status_code == 200


