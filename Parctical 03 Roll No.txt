# Node class
class Node:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.prev = None
        self.next = None

head = None

# Insert student in sorted order
def insert():
    global head
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")

    newnode = Node(roll, name)

    if head is None:
        head = newnode
    elif roll < head.roll:
        newnode.next = head
        head.prev = newnode
        head = newnode
    else:
        temp = head
        while temp.next and temp.next.roll < roll:
            temp = temp.next

        newnode.next = temp.next
        newnode.prev = temp

        if temp.next:
            temp.next.prev = newnode

        temp.next = newnode

    print("Student inserted successfully!")

# Delete student by roll number
def delete():
    global head
    roll = int(input("Enter Roll No to delete: "))

    temp = head

    while temp:
        if temp.roll == roll:
            if temp.prev:
                temp.prev.next = temp.next
            else:
                head = temp.next

            if temp.next:
                temp.next.prev = temp.prev

            print("Student deleted successfully!")
            return

        temp = temp.next

    print("Student not found!")

# Display forward
def forward():
    temp = head

    while temp:
        print(temp.roll, temp.name)
        temp = temp.next

# Display backward
def backward():
    temp = head

    if temp is None:
        print("No student records!")
        return

    while temp.next:
        temp = temp.next

    while temp:
        print(temp.roll, temp.name)
        temp = temp.prev

# Main function
def main():
    while True:
        print("\n1. Insert Student")
        print("2. Delete Student")
        print("3. Display Forward")
        print("4. Display Backward")
        print("5. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            insert()
        elif ch == 2:
            delete()
        elif ch == 3:
            forward()
        elif ch == 4:
            backward()
        elif ch == 5:
            break
        else:
            print("Invalid Choice!")

main()