# Student Management System

students = []

print("===== Student Management System =====")

name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")

student = {
    "name": name,
    "age": age,
    "course": course
}

students.append(student)

print("\nStudent added successfully!")
print("Student Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
