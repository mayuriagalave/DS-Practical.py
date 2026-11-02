# Array
marks = []

# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

# Insert marks in both structures
def insert():
    global head
    m = int(input("Enter IA Marks: "))

    marks.append(m)

    newnode = Node(m)

    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    print("Marks inserted successfully!")

# Display Array and Linked List
def display():
    print("Array Representation:")
    for i in range(len(marks)):
        print("Index", i, ":", marks[i])

    print("Linked List Representation:")
    temp = head
    while temp:
        print(temp.data, "->", end=" ")
        temp = temp.next
    print("None")

# Count students scoring more than 80
def count():
    c = 0
    for m in marks:
        if m > 80:
            c += 1

    print("Students scoring above 80:", c)

# Main function
def main():
    while True:
        print("\n1. Insert Marks")
        print("2. Display Marks")
        print("3. Count Marks Above 80")
        print("4. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            insert()
        elif ch == 2:
            display()
        elif ch == 3:
            count()
        elif ch == 4:
            break
        else:
            print("Invalid Choice!")

main()