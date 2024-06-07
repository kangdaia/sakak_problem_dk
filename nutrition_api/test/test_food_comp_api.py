import time


def test_root(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == ['CONNECT']


def test_create_get_food_comp(test_client, test_obj):
    response = test_client.post(
            "/api/v1/food_comp/",
            json=test_obj
        )
    assert response.status_code == 201
    #duplicate exception check
    response = test_client.post(
        "/api/v1/food_comp/",
        json=test_obj
    )
    assert response.status_code == 400
    params = {
        "food_cd": test_obj["food_cd"]
    }
    response = test_client.get(f"/api/v1/food_comp/search", params=params)
    assert response.status_code == 200
    assert response.json()["Status"] == "Success"


def test_create_update_food_comp(test_client, test_obj, mod_obj):
    response = test_client.post("/api/v1/food_comp/", json=test_obj)
    assert response.status_code == 201

    time.sleep(1)
    response = test_client.patch(
        f"/api/v1/food_comp/{test_obj['food_cd']}", json=mod_obj
    )
    assert response.status_code == 200