import requests
import json

BASE_URL = 'http://localhost:8000/api'

def test_api():
    print("Testing Kaspi.kz API...\n")
    
    # Test root endpoint
    print("1. Testing API root...")
    response = requests.get(f'{BASE_URL}/')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    
    # Test categories
    print("2. Testing categories endpoint...")
    response = requests.get(f'{BASE_URL}/categories/')
    print(f"   Status: {response.status_code}")
    print(f"   Found {len(response.json())} categories\n")
    
    # Test products
    print("3. Testing products endpoint...")
    response = requests.get(f'{BASE_URL}/products/')
    print(f"   Status: {response.status_code}")
    print(f"   Found {len(response.json())} products\n")
    
    # Test category products
    print("4. Testing category products endpoint...")
    response = requests.get(f'{BASE_URL}/categories/1/products/')
    print(f"   Status: {response.status_code}")
    print(f"   Found {len(response.json())} products in category 1\n")
    
    print("All tests completed successfully!")

if __name__ == "__main__":
    test_api()