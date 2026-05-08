try:
    import requests  # type: ignore
except ImportError:
    print("Error: 'requests' module not found. Install it with: pip install requests")
    exit(1)

BASE_URL = "http://127.0.0.1:8000"

def test():
    print("=== Testing FastAPI Item API ===\n")

    # 1. CREATE
    print("1. CREATE an item")
    item_data = {
        "name": "Laptop",
        "description": "A powerful laptop",
        "price": 999.99,
        "is_offer": True
    }
    resp = requests.post(f"{BASE_URL}/items/", json=item_data)
    print(f"Status: {resp.status_code}, Response: {resp.json()}")
    assert resp.status_code == 201
    created_id = resp.json()["id"]

    # 2. READ ALL
    print("\n2. READ all items")
    resp = requests.get(f"{BASE_URL}/items/")
    print(f"Status: {resp.status_code}, Count: {len(resp.json())}")

    # 3. READ ONE
    print(f"\n3. READ item {created_id}")
    resp = requests.get(f"{BASE_URL}/items/{created_id}")
    print(f"Status: {resp.status_code}, Response: {resp.json()}")

    # 4. PARTIAL UPDATE (only change price)
    print(f"\n4. PARTIAL UPDATE item {created_id} (price to 899.99)")
    resp = requests.put(f"{BASE_URL}/items/{created_id}", json={"price": 899.99})
    print(f"Status: {resp.status_code}, Updated: {resp.json()}")
    # Verify that name and description didn't change
    updated = resp.json()
    assert updated["name"] == "Laptop"
    assert updated["description"] == "A powerful laptop"
    assert updated["price"] == 899.99

    # 5. DELETE
    print(f"\n5. DELETE item {created_id}")
    resp = requests.delete(f"{BASE_URL}/items/{created_id}")
    print(f"Status: {resp.status_code}, Response: {resp.json()}")

    # 6. VERIFY DELETION (should be 404)
    print(f"\n6. VERIFY item {created_id} is gone")
    resp = requests.get(f"{BASE_URL}/items/{created_id}")
    print(f"Status: {resp.status_code} (expected 404)")

    print("\n=== All tests passed! ===")

if __name__ == "__main__":
    test()