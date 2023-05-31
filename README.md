# Bookstore API

This is a RESTful API for a bookstore, built with FastAPI and MongoDB. It allows you to manage authors, books, and reviews.

## Requirements

- Python 3.6+
- FastAPI
- pymongo

## Installation

1. Clone the repository:

```
git clone <repository_url>
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Configure MongoDB:

- Install MongoDB on your system or use a cloud-based MongoDB service.
- Update the MongoDB connection URL in the `mongo_client` variable in the `main.py` file to connect to your MongoDB instance.

## Usage

1. Start the API server:

```
uvicorn main:app --reload
```

2. The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs). You can use the Swagger UI or ReDoc interface to explore and test the available endpoints.

3. Available endpoints:

- **POST /authors**: Create a new author.
- **GET /authors**: Get a list of all authors.
- **GET /authors/{author_id}**: Get details of a specific author.
- **PATCH /authors/{author_id}**: Update an existing author.
- **DELETE /authors/{author_id}**: Delete an author.

- **POST /books**: Create a new book.
- **GET /books**: Get a list of all books. You can also filter books by author.
- **GET /books/{book_id}**: Get details of a specific book.
- **PATCH /books/{book_id}**: Update an existing book.
- **DELETE /books/{book_id}**: Delete a book.

4. The API is pre-seeded with some data for authors, books, and reviews. You can modify the `seed_data()` function in `main.py` to add more data or modify the existing data.

