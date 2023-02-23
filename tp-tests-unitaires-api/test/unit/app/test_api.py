from test.unit.app import client, new_user1, new_user2, update_user

def test_create(client, new_user1):
    response = client.post("/create", json=new_user1)
    assert response.status_code == 200
    assert response.data.decode() == 'true'

def test_read(client, new_user1):
    response = client.get("/select/1")
    assert response.status_code == 200
    assert response.get_json() == new_user1

def test_read_all(client, new_user1, new_user2):
    client.post("/create", json=new_user2)
    response = client.get("/select")
    assert response.status_code == 200
    assert len(response.get_json()) == 2
    assert response.get_json()[0] == new_user1
    assert response.get_json()[1] == new_user2

def test_update(client, update_user):
    response = client.put("/update", json=update_user)
    assert response.status_code == 200
    assert response.data.decode() == 'true'
    response = client.get("/select/"+str(update_user["id"]))
    assert response.get_json() == update_user

def test_delete(client):
    response = client.delete("/delete/1")
    assert response.status_code == 200
    assert response.data.decode() == 'true'
    response = client.get("/select/1")
    assert response.get_json() == None