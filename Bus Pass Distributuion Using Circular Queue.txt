# Circular Queue
size = 5
queue = [None] * size
front = -1
rear = -1

# Insert student ID
def enqueue():
    global front, rear

    if (rear + 1) % size == front:
        print("Queue is Full!")
    else:
        id = int(input("Enter Student ID: "))

        if front == -1:
            front = 0

        rear = (rear + 1) % size
        queue[rear] = id

        print("Student added successfully!")

# Delete student ID
def dequeue():
    global front, rear

    if front == -1:
        print("Queue is Empty!")
    else:
        print("Pass Issued to Student:", queue[front])

        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % size

# Display circular queue
def display():
    if front == -1:
        print("Queue is Empty!")
    else:
        print("Circular Queue:")
        i = front

        while True:
            print(queue[i], end=" ")
            if i == rear:
                break
            i = (i + 1) % size

        print()

# Main function
def main():
    while True:
        print("\n1. Insert Student ID")
        print("2. Issue Bus Pass")
        print("3. Display Queue")
        print("4. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            enqueue()
        elif ch == 2:
            dequeue()
        elif ch == 3:
            display()
        elif ch == 4:
            break
        else:
            print("Invalid Choice!")

main()