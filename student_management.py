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


# Display all students
print("\n===== All Student Details =====")

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("-------------------------")


# Search for a student
search_name = input("\nEnter student name to search: ")

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("\nStudent Found!")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        found = True
        break

if not found:
    print("Student not found.")
