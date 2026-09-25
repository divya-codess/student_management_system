# Student Management System

students = []

number_of_students = int(input("How many students do you want to add? "))

for i in range(number_of_students):

    print("\nEnter details for student", i + 1)

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

print("\n===== Student Details =====")

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("-------------------------")
