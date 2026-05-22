from fastapi.testclient import TestClient
from src.main import app
import uuid

client = TestClient(app)

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_book():

    data = {
        "title": f"Test Book {uuid.uuid4()}",
        "author": "Author",
        "genre": "Tech",
        "total_copies": 2,
        "available_copies": 2
    }

    create_response = client.post("/books/", json=data)

    print(create_response.status_code)
    print(create_response.json())

    book_id = create_response.json()["id"]

    response = client.get(f"/books/{book_id}")

    assert response.status_code == 200


def test_delete_book():

    data = {
        "title": "Delete Book",
        "author": "Author",
        "genre": "Tech",
        "total_copies": 1,
        "available_copies": 1
    }

    create_response = client.post("/books/", json=data)

    book_id = create_response.json()["id"]

    response = client.delete(f"/books/{book_id}")

    assert response.status_code == 200