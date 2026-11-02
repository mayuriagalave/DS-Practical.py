students = []

# Insert student records
def insert():
    n = int(input("Enter number of students: "))

    for i in range(n):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        div = input("Enter Division: ")
        students.append([roll, name, div])

# Linear Search by Name
def linear_search():
    name = input("Enter Name to search: ")
    count = 0

    for s in students:
        count += 1
        if s[1].lower() == name.lower():
            print("Student Found:", s)
            print("Comparisons:", count)
            return

    print("Student Not Found!")
    print("Comparisons:", count)

# Binary Search by Roll No
def binary_search():
    students.sort(key=lambda x: x[0])

    roll = int(input("Enter Roll No to search: "))
    low = 0
    high = len(students) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1

        if students[mid][0] == roll:
            print("Student Found:", students[mid])
            print("Comparisons:", count)
            return
        elif students[mid][0] < roll:
            low = mid + 1
        else:
            high = mid - 1

    print("Student Not Found!")
    print("Comparisons:", count)

# Display all students
def display():
    for s in students:
        print(s)

# Main function
def main():
    insert()

    while True:
        print("\n1. Linear Search")
        print("2. Binary Search")
        print("3. Display Students")
        print("4. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            linear_search()
        elif ch == 2:
            binary_search()
        elif ch == 3:
            display()
        elif ch == 4:
            break
        else:
            print("Invalid Choice!")

main()