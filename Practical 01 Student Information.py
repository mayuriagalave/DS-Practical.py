students = []

# Insert a new student at a given position
def insert_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    cgpa = float(input("Enter CGPA: "))
    pos = int(input("Enter Position: "))

    student = [roll, name, cgpa]
    students.insert(pos - 1, student)
    print("Student inserted successfully!")

# Delete student by roll number
def delete_student():
    roll = int(input("Enter Roll No to delete: "))

    for s in students:
        if s[0] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found!")

# Search student by roll number
def search_student():
    roll = int(input("Enter Roll No to search: "))

    for s in students:
        if s[0] == roll:
            print("Roll No:", s[0])
            print("Name:", s[1])
            print("CGPA:", s[2])
            return

    print("Student not found!")

# Display all students
def display_students():
    if len(students) == 0:
        print("No student records!")
    else:
        for s in students:
            print(s)

# Main function
def main():
    while True:
        print("\n1. Insert Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. Display Students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            insert_student()
        elif choice == 2:
            delete_student()
        elif choice == 3:
            search_student()
        elif choice == 4:
            display_students()
        elif choice == 5:
            print("Program Ended!")
            break
        else:
            print("Invalid Choice!")

main()