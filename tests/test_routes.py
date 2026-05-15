import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app("testing")
    return app.test_client()


def test_index(client):
    res = client.get("/")
    assert res.status_code == 200


def test_health_check(client):
    res = client.get("/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "healthy"


def test_readiness(client):
    res = client.get("/ready")
    assert res.status_code == 200


def test_get_items(client):
    res = client.get("/api/items")
    assert res.status_code == 200
    assert "items" in res.get_json()


def test_item_not_found(client):
    res = client.get("/api/items/999")
    assert res.status_code == 404


def test_create_item(client):
    res = client.post("/api/items", json={"name": "Test Item"})
    assert res.status_code == 201
    assert res.get_json()["name"] == "Test Item"