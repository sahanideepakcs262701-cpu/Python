# Student ADT using Command Line

students = []

def create_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age
    }

    students.append(student)
    print("Student Added Successfully!")

def update_student():
    roll = input("Enter Roll No to Update: ")

    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")

def delete_student():
    roll = input("Enter Roll No to Delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

def display_students():
    print("\nStudent Records:")
    for student in students:
        print(student)

while True:
    print("\n----- Student ADT Menu -----")
    print("1. Create Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        break
    else:
        print("Invalid Choice!")
