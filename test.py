import requests

BASE_URL = "http://localhost:8000"  


def get_authors():
    url = f"{BASE_URL}/authors"
    response = requests.get(url)
    if response.status_code == 200:
        authors = response.json()
        print("Authors:")
        for author in authors:
            print(f"Author ID: {author['_id']}, Name: {author['name']}")
    else:
        print("Failed to retrieve authors.")

def update_author(author_id, name=None, address=None, age=None):
    url = f"{BASE_URL}/authors/{author_id}"
    data = {}
    if name:
        data["name"] = name
    if address:
        data["address"] = address
    if age:
        data["age"] = age
    response = requests.patch(url, json=data)
    if response.status_code == 200:
        print("Author updated successfully.")
    elif response.status_code == 404:
        print("Author not found.")
    else:
        print("Failed to update author.")




update_author(author_id="64778781f1957645b7eec86c", name="John Smith") 
get_authors()

