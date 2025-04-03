from app import app

def test_homepage_returns_welcome_message():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"message": "Welcome to the Product Catalog API!"}

def test_get_all_products_returns_list():
    client = app.test_client()
    response = client.get("/products")
    assert response.status_code == 200
    assert response.is_json
    products = response.get_json()
    assert isinstance(products, list)
    assert len(products) >= 1

def test_get_product_by_id_returns_expected_product():
    client = app.test_client()
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.is_json
    product = response.get_json()
    assert "id" in product and product["id"] == 1

def test_get_product_by_invalid_id_returns_404():
    client = app.test_client()
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.is_json
    assert response.get_json()["error"] == "Product not found"

def test_query_param_filtering_by_category():
    client = app.test_client()
    response = client.get("/products?category=books")
    assert response.status_code == 200
    assert response.is_json
    filtered = response.get_json()
    assert isinstance(filtered, list)
    for product in filtered:
        assert product["category"].lower() == "books"
