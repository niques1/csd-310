

from pymongo import MongoClient

# Connect to the MongoDB instance
client = MongoClient("mongodb+srv://admin:admin@cluster0.gq8ezkg.mongodb.net/?retryWrites=true&w=majority")

# Get the Pytech database
db = client.pytech_db

# Get the students collection
collection = db["students"]

# Find all documents in the collection
all_students = collection.find()

# Find all documents in the collection and display them
print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")

cursor = collection.find({})
for document in cursor:
    print("\nStudent ID:", document["student_id"])
    print("First Name:", document["first_name"])
    print("Last Name:", document["last_name"])

# Insert a new document into the collection
new_student = { "student_id": 1010, "first_name": "Steven", "last_name": "Greens" }
result = collection.insert_one(new_student)

print("\n-- INSERT STATEMENTS--")
print("Inserted student record into the students collection with document id", result.inserted_id)

# Find a single document by student_id and display it
student = collection.find_one({"student_id": 1010})
print("\n-- DISPLAYING STUDENT TEST DOC")
print("\nStudent ID:", student["student_id"])
print("First Name:", student["first_name"])
print("Last Names", student["last_name"])

# Delete the document by student_id
collection.delete_one({"student_id": 1010})

# Find all documents in the collection and display them
print("\n--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")
cursor = collection.find({})
for document in cursor:
    print("\nStudent ID:", document["student_id"])
    print("First Name:", document["first_name"])
    print("Last Name:", document["last_name"])

print("\nEnd of program, press any key to continue...")
