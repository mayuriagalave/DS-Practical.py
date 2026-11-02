queue = []
count = 0

# Insert student
def insert():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: "))
    cgpa = float(input("Enter CGPA: "))

    student = [roll, name, cgpa]
    queue.append(student)

    queue.sort(key=lambda x: x[2], reverse=True)

    print("Student inserted!")
    display()

# Delete highest CGPA student
def delete():
    global count

    if len(queue) == 0:
        print("Queue is Empty!")
    else:
        student = queue.pop(0)
        print("Processed Student:", student)
        count += 1
        display()

# Display queue
def display():
    print("Priority Queue:")
    for s in queue:
        print(s)

# Main function
def main():
    while True:
        print("\n1. Insert Student")
        print("2. Delete Highest CGPA")
        print("3. Display Queue")
        print("4. Count Processed Students")
        print("5. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            insert()
        elif ch == 2:
            delete()
        elif ch == 3:
            display()
        elif ch == 4:
            print("Students Processed:", count)
        elif ch == 5:
            break
        else:
            print("Invalid Choice!")

main()