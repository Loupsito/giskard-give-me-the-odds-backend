from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_concatenate_strings():
    response = client.post(
        "/concatenate_strings",
        json={"string1": "Hello", "string2": "World"},
    )
    assert response.status_code == 200
    assert response.json() == "HelloWorld"

    response = client.post(
        "/concatenate_strings",
        json={"string1": "Fast", "string2": "API"},
    )
    assert response.status_code == 200
    assert response.json() == "FastAPI"
