
# pytech_insert

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.gq8ezkg.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech_db"]
students = db["students"]

# Insert three new student documents
student1 = {
 "student_id": 1007,
 "first_name": "Royal",
 "last_name": "Blues",
 "email": "royalblues@gmail.com",
 "age": 22,
 "gender": "Male",
 "enrolled": True
}
student2 = {
 "student_id": 1008,
 "first_name": "Nicholas",
 "last_name": "Purples",
 "email": "nicholaspurples@gmail.com",
 "age": 24,
 "gender": "Female",
 "enrolled": False
}
student3 = {
 "student_id": 1009,
 "first_name": "Lorena",
 "last_name": "Yellows",
 "email": "lorenayellows@gmail.com",
 "age": 26,
 "gender": "Male",
 "enrolled": True
}

student1_id = students.insert_one(student1).inserted_id
student2_id = students.insert_one(student2).inserted_id
student3_id = students.insert_one(student3).inserted_id

print("Student 1 ID:", student1_id)
print("Student 2 ID:", student2_id)
print("Student 3 ID:", student3_id)
