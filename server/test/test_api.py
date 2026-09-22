from server import app

def test_healthz_route():
    client = app.test_client()
    resp = client.get("/healthz")

    assert resp.status_code == 200
    assert resp.is_json


def test_delete_document_rejects_non_integer_id():
    client = app.test_client()
    resp = client.delete("/api/delete-document?id=1 OR 1=1")

    assert resp.status_code == 400
    assert resp.get_json() == {"error": "document id required"}
    
