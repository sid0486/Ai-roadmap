from fastapi.testclient import TestClient
from src.main import app
import uuid

client = TestClient(app)

def test_get_members():

    response = client.get("/members/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_member():

    data = {
    "name": "John Doe",
    "email": f"john{uuid.uuid4()}@gmail.com",
    "phone": "9876543210",
    "membership_type": "basic",
    "password": "john123"}

    response = client.post("/members/", json=data)

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


def test_get_member():

    data = {
        "name": "Alicep",
        "email": f"alice{uuid.uuid4()}@gmail.com",
        "phone": "9876544210",
        "membership_type": "basic",
        "password": "alice111"
    }

    create_response = client.post("/members/", json=data)

    print(create_response.status_code)
    print(create_response.json())

    member_id = create_response.json()["id"]

    response = client.get(f"/members/{member_id}")

    assert response.status_code == 200


def test_delete_member():

    data = {
        "name": "Delete Usser",
        "email": f"delete{uuid.uuid4()}@gmail.com",
        "phone": "9873242210",
        "membership_type": "basic",
        "password": "delete132"
    }

    create_response = client.post("/members/", json=data)

    print(create_response.status_code)
    print(create_response.json())

    member_id = create_response.json()["id"]

    response = client.delete(f"/members/{member_id}")

    assert response.status_code == 200