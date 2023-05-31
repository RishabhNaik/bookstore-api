import requests

# Specify the API endpoint URL
url = "http://localhost:8000/authors"

# Define the author details
author_data = {
    "name": "John Doe",
    "address": "123 Main St, City, Country",
    "age": 35
}

# Send a POST request to create the author
response = requests.post(url, json=author_data)

# Check the response status code
if response.status_code == 201:
    # Author creation successful
    author_id = response.json().get("author_id")
    print("Author created with ID:", author_id)
else:
    # Error occurred
    print("Failed to create author:", response.json())
