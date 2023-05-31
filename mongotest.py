from pymongo import MongoClient

# MongoDB configuration
mongo_client = MongoClient("mongodb://localhost:27017")
db = mongo_client["Bookstore"]
authors_collection = db["authors"]
books_collection = db["books"]
reviews_collection = db["reviews"]

# print(mongo_client)

# print(db)

print(list(authors_collection.find()))