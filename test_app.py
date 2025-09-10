import os
import pytest
from app import app, db, Entry

@pytest.fixture
def client():
    # Use an in-memory SQLite database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_hello_endpoint_with_db(client):
    # Send a GET request to the root URL
    response = client.get("/")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the database entry was created
    with app.app_context():
        assert Entry.query.count() == 1

    # Check the response message
    assert b"Successfully added a new entry to the database!" in response.data
