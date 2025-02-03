import requests

database = {
    1: "Aice",
    2: "Bob",
    3: "Charlie"
}


def get_user_from_db(user_id: int):
    return database.get(user_id)


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError