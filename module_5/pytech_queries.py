
# pytech_queries

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.gq8ezkg.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech_db"]
students = db["students"]

# Display all documents in the collection
docs = students.find({})
for doc in docs:
    print(doc)

# Display a single document by student_id
student = students.find_one({"student_id": 1007})
print("Student with ID 1007:", student)
