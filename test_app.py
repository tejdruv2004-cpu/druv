from app import app


def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_response_contains_hello_world():
    client = app.test_client()
    response = client.get("/")
    assert b"Hello World Thavamani Thapasuraman" in response.data
