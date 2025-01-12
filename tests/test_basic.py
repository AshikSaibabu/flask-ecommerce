import pytest
from flask_app import create_app


@pytest.fixture
def app():
    """Fixture for creating the Flask app for testing."""
    app = create_app()
    app.config.update({
        "TESTING": True,  # Enables testing mode
    })
    return app


@pytest.fixture
def client(app):
    """Fixture for accessing the Flask test client."""
    return app.test_client()


def test_home_page(client):
    """Test the home page route."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data
