from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId

mongo_client = MongoClient("localhost")
db = mongo_client["Bookstore"]
authors_collection = db["authors"]
books_collection = db["books"]
reviews_collection = db["reviews"]

app = FastAPI()

class Author:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age


class Book:
    def __init__(self, name, author, genre, published_date):
        self.name = name
        self.author = author
        self.genre = genre
        self.published_date = published_date


class Review:
    def __init__(self, book_id, reviewer, rating, comments):
        self.book_id = ObjectId(book_id) 
        self.reviewer = reviewer
        self.rating = rating
        self.comments = comments


@app.post("/authors")
def create_author(name: str, address: str, age: int):
    author = Author(name, address, age)
    author_id = authors_collection.insert_one(author.__dict__).inserted_id
    return {"author_id": str(author_id)}


@app.get("/authors")
def get_authors():
    authors = []
    for author in authors_collection.find({}):
        author['_id'] = str(author['_id'])
        authors.append(author)
    return authors


@app.get("/authors/{author_id}")
def get_author(author_id: str):
    author = authors_collection.find_one({"_id": ObjectId(author_id)})
    if author:
        return author
    else:
        raise HTTPException(status_code=404, detail="Author not found")


@app.patch("/authors/{author_id}")
def update_author(author_id: str, name: str = None, address: str = None, age: int = None):
    author = authors_collection.find_one({"_id": ObjectId(author_id)})
    if author:
        if name:
            author["name"] = name
        if address:
            author["address"] = address
        if age:
            author["age"] = age
        authors_collection.update_one({"_id": ObjectId(author_id)}, {"$set": author}) 
        return {"message": "Author updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Author not found")


@app.delete("/authors/{author_id}")
def delete_author(author_id: str):
    result = authors_collection.delete_one({"_id": ObjectId(author_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}


@app.post("/books")
def create_book(name: str, author: str, genre: str, published_date: str):
    book = Book(name, author, genre, published_date)
    book_id = books_collection.insert_one(book.__dict__).inserted_id
    return {"book_id": str(book_id)}


@app.get("/books")
def get_books(author: str = None):
    if author:
        books = list(books_collection.find({"author": author}))
    else:
        books = list(books_collection.find())
    return books


@app.get("/books/{book_id}")
def get_book(book_id: str):
    book = books_collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@app.patch("/books/{book_id}")
def update_book(book_id: str, name: str = None, author: str = None, genre: str = None, published_date: str = None):
    book = books_collection.find_one({"_id": ObjectId(book_id)})
    if book:
        if name:
            book["name"] = name
        if author:
            book["author"] = author
        if genre:
            book["genre"] = genre
        if published_date:
            book["published_date"] = published_date
        books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": book})
        return {"message": "Book updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    result = books_collection.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}


@app.post("/reviews")
def create_review(book_id: str, reviewer: str, rating: int, comments: str):
    review = Review(book_id, reviewer, rating, comments)
    review_id = reviews_collection.insert_one(review.__dict__).inserted_id
    return {"review_id": str(review_id)}


@app.get("/reviews")
def get_reviews(book_id: str = None):
    if book_id:
        reviews = list(reviews_collection.find({"book_id": ObjectId(book_id)})) 
    else:
        reviews = list(reviews_collection.find())
    return reviews


@app.get("/reviews/{review_id}")
def get_review(review_id: str):
    review = reviews_collection.find_one({"_id": ObjectId(review_id)})  
    if review:
        return review
    else:
        raise HTTPException(status_code=404, detail="Review not found")


@app.patch("/reviews/{review_id}")
def update_review(review_id: str, rating: int = None, comments: str = None):
    review = reviews_collection.find_one({"_id": ObjectId(review_id)})  
    if review:
        if rating:
            review["rating"] = rating
        if comments:
            review["comments"] = comments
        reviews_collection.update_one({"_id": ObjectId(review_id)}, {"$set": review}) 
        return {"message": "Review updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Review not found")


@app.delete("/reviews/{review_id}")
def delete_review(review_id: str):
    result = reviews_collection.delete_one({"_id": ObjectId(review_id)}) 
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Review not found")
    return {"message": "Review deleted successfully"}


@app.on_event("startup")
def seed_data():
    authors = [
        Author("Author 1", "Address 1", 30),
        Author("Author 2", "Address 2", 35),
    ]
    authors_collection.insert_many([author.__dict__ for author in authors])

    books = [
        Book("Book 1", "Author 1", "Genre 1", "2022-01-01"),
        Book("Book 2", "Author 2", "Genre 2", "2022-02-02"),
    ]
    books_collection.insert_many([book.__dict__ for book in books])

    reviews = [
        Review(str(books[0]._id), "Reviewer 1", 5, "Great book!"),
        Review(str(books[0]._id), "Reviewer 2", 4, "Enjoyed reading it."),
    ]
    reviews_collection.insert_many([review.__dict__ for review in reviews])
