def test_ping(client):
    res = client.get('api/ping')
    assert res.status_code == 200
