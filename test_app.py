from app import app

def test_hello_endpoint():
    # Create a test client to simulate requests to the app
    client = app.test_client()

    # Send a GET request to the root URL
    response = client.get("/")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response data contains the correct message
    assert b"Hello, DevOps from Flask!" in response.data
