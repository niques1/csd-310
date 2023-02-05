

from pymongo import MongoClient

url = ("mongodb+srv://admin:admin@cluster0.gq8ezkg.mongodb.net/?retryWrites=true&w=majority")

# Connect to the MongoDB instance
client = MongoClient(url)

# Get the Pytech database
db = client.pytech_db

# Get the students collection
students_collection = db["students"]

# Find all documents in the collection
all_students = students_collection.find()

# Output all documents
print("Before Update:")
for student in all_students:
    print(student)

# Update the last_name of student with student_id 1007
result = students_collection.update_one({"student_id": 1007}, {"$set": {"last_name": "Purples"}})

# Find and output the updated document
updated_student = students_collection.find_one({"student_id": 1007})
print("\nAfter Update:")
print(updated_student)
