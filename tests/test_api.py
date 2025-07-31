from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_full_flow():
    resp = client.post("/shorten", params={"target_url": "https://example.com"})
    slug = resp.json()["short_url"].lstrip("/")
    resp2 = client.get(f"/stats/{slug}")
    assert resp2.json()["clicks"] == 0

    client.get(f"/{slug}")
    resp3 = client.get(f"/stats/{slug}")
    assert resp3.json()["clicks"] == 1
