import time


def test_root(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == ['CONNECT']


def test_create_get_food_comp(test_client, food_comp_test_obj):
    response = test_client.post(
            "/api/v1/food_comp/",
            json=food_comp_test_obj
        )
    assert response.status_code == 201
    #duplicate exception check
    response = test_client.post(
        "/api/v1/food_comp/",
        json=food_comp_test_obj
    )
    assert response.status_code == 400
    params = {
        "food_code": food_comp_test_obj["food_code"]
    }
    response = test_client.get(f"/api/v1/food_comp/search", params=params)
    assert response.status_code == 200


def test_create_update_delete_food_comp(test_client, food_comp_test_obj, food_comp_test_obj_update):
    response = test_client.post("/api/v1/food_comp/", json=food_comp_test_obj)
    assert response.status_code == 201

    time.sleep(1)
    response = test_client.put(
        f"/api/v1/food_comp/{food_comp_test_obj['food_code']}", json=food_comp_test_obj_update
    )
    assert response.status_code == 200
    
    time.sleep(1)
    response = test_client.delete(f"/api/v1/food_comp/{food_comp_test_obj['food_code']}")
    assert response.status_code == 204