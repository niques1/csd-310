

from pymongo import MongoClient

# Connect to the MongoDB instance
client = MongoClient("mongodb+srv://admin:admin@cluster0.gq8ezkg.mongodb.net/?retryWrites=true&w=majority")

# Get the Pytech database
db = client.pytech_db

# Get the students collection
students_collection = db["students"]

# Find all documents in the collection
all_students = students_collection.find()

# Output all documents
print("\n--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")
for student in all_students:

    print("\nStudent ID:", student["student_id"])

    print("First Name:", student["first_name"])

    print("Last Name:", student["last_name"])

# Update the last_name of student with student_id 1007
result = students_collection.update_one({"student_id": 1007}, {"$set": {"last_name": "Gods"}})

# Find and output the updated document
updated_student = students_collection.find_one({"student_id": 1007})

print("\n-- DISPLAYING STUDENT DOCUMENT 1007--")
print("\nStudent ID:", updated_student["student_id"])
print("First Name:", updated_student["first_name"])
print("Last Name:", updated_student["last_name"])
