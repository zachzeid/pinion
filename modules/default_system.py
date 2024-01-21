# modules/example_system.py
import requests

# Base URL for the system's API
BASE_URL = "https://example-system.com/api"

def list_users():
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to list users: {response.status_code}, {response.text}")

def add_user(user_info):
    url = f"{BASE_URL}/users"
    response = requests.post(url, json=user_info)
    if response.status_code == 201:
        print(f"User added successfully: {response.json()}")
    else:
        raise Exception(f"Failed to add user: {response.status_code}, {response.text}")

def disable_user(user_info):
    email = user_info.get('email')
    url = f"{BASE_URL}/users/{email}/disable"
    response = requests.patch(url)
    if response.status_code == 200:
        print(f"User disabled successfully")
    else:
        raise Exception(f"Failed to disable user: {response.status_code}, {response.text}")

def delete_user(user_info):
    email = user_info.get('email')
    url = f"{BASE_URL}/users/{email}"
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"User deleted successfully")
    else:
        raise Exception(f"Failed to delete user: {response.status_code}, {response.text}")

# Example usage
if __name__ == "__main__":
    test_user = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
    }

    # Uncomment these lines to test the functions
    # print(list_users())
    # add_user(test_user)
    # disable_user(test_user)
    # delete_user(test_user)
