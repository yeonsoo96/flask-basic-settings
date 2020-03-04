def test_get_test(client):
    res = client.get('/api/test')
    assert res.status_code == 200


def test_post_test(client):
    res = client.post('/api/test')
    assert res.status_code == 200


def test_put_test(client):
    res = client.put('/api/test')
    assert res.status_code == 200


def test_delete_test(client):
    res = client.delete('/api/test')
    assert res.status_code == 200