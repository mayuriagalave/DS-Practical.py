queue = []

# Enqueue student token
def enqueue():
    token = int(input("Enter Student Token Number: "))
    queue.append(token)
    print("Student added to queue!")

# Dequeue student
def dequeue():
    if len(queue) == 0:
        print("Queue is Empty!")
    else:
        token = queue.pop(0)
        print("Student Processed:", token)

# Display Front and Rear
def front_rear():
    if len(queue) == 0:
        print("Queue is Empty!")
    else:
        print("Front Token:", queue[0])
        print("Rear Token:", queue[-1])

# Display complete queue
def display():
    print("Admission Queue:", queue)

# Main function
def main():
    while True:
        print("\n1. Enqueue Student")
        print("2. Dequeue Student")
        print("3. Display Front and Rear")
        print("4. Display Queue")
        print("5. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            enqueue()
        elif ch == 2:
            dequeue()
        elif ch == 3:
            front_rear()
        elif ch == 4:
            display()
        elif ch == 5:
            break
        else:
            print("Invalid Choice!")

main()