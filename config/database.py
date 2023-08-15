from pymongo import MongoClient

client = MongoClient("mongodb+srv://<your username>:<password>@cluster0.slhdetl.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db 

collection_name = db["todo_collection"]
