import json

def menu():
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    with open("students.json", "r") as file:
        students = json.load(file)

    students.append(student)

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Student added successfully!")

def view_student():
    with open("students.json", "r") as file:
        students = json.load(file)

    print("===== Student List =====")

    for index, student in enumerate(students, start=1):
        print("\nStudent", index)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])

def search_student():
    search_name = input("Enter student name to search: ")

    with open("students.json", "r") as file:
        students = json.load(file)

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("Student Found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            found = True

    if found == False:
        print("Student not found")

def delete_student():
    delete_name = input("Enter student name to delete: ")

    with open("students.json", "r") as file:
        students = json.load(file)

    updated_students = []

    for student in students:
        if student["name"].lower() != delete_name.lower():
            updated_students.append(student)

    with open("students.json", "w") as file:
        json.dump(updated_students, file, indent=4)

    print("Student deleted successfully!")

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("❌ Invalid choice! Please enter a number from 1 to 5.")