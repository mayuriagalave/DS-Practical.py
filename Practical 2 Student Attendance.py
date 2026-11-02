 # Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

# Insert attendance at the end
def insert():
    global head
    data = input("Enter Attendance (P/A): ").upper()
    newnode = Node(data)

    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    print("Attendance inserted!")

# Update attendance of a given day
def update():
    day = int(input("Enter Day: "))
    data = input("Enter New Attendance (P/A): ").upper()

    temp = head
    count = 1

    while temp:
        if count == day:
            temp.data = data
            print("Attendance updated!")
            return
        temp = temp.next
        count += 1

    print("Day not found!")

# Count Present and Absent days
def count():
    p = 0
    a = 0
    temp = head

    while temp:
        if temp.data == "P":
            p += 1
        elif temp.data == "A":
            a += 1
        temp = temp.next

    print("Present Days:", p)
    print("Absent Days:", a)

# Display attendance list
def display():
    temp = head
    day = 1

    while temp:
        print("Day", day, ":", temp.data)
        temp = temp.next
        day += 1

    if head is None:
        print("No attendance records!")

# Main function
def main():
    while True:
        print("\n1. Insert Attendance")
        print("2. Update Attendance")
        print("3. Count Present and Absent")
        print("4. Display Attendance")
        print("5. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            insert()
        elif ch == 2:
            update()
        elif ch == 3:
            count()
        elif ch == 4:
            display()
        elif ch == 5:
            break
        else:
            print("Invalid Choice!")

main()