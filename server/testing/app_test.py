from app import app
import pytest


@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client


def test_index(client):
    response = client.get("/")
    assert b"Python Operations with Flask Routing and Views" in response.data


def test_print_string(client):
    response = client.get("/print/Hello")
    assert b"Hello" in response.data


def test_count(client):
    response = client.get("/count/3")
    assert b"0\n1\n2\n3" in response.data


def test_math(client):
    response = client.get("/math/2+3")
    assert b"Result: 5" in response.data
