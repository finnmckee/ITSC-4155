import pytest
from fastapi.testclient import TestClient
from kitchen.main import app   # NOTE: absolute import from the package

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c