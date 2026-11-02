from collections import deque

dq = deque()

# Add emergency case at front
def emergency():
    name = input("Enter Student Name: ")
    dq.appendleft(name)
    print("Emergency case added!")
    display()

# Add normal case at rear
def normal():
    name = input("Enter Student Name: ")
    dq.append(name)
    print("Normal case added!")
    display()

# Serve student from front
def serve():
    if len(dq) == 0:
        print("Deque is Empty!")
    else:
        print("Serving Student:", dq.popleft())
    display()

# Display deque
def display():
    print("Service Queue:", list(dq))

# Main function
def main():
    while True:
        print("\n1. Add Emergency Case")
        print("2. Add Normal Case")
        print("3. Serve Student")
        print("4. Display Deque")
        print("5. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            emergency()
        elif ch == 2:
            normal()
        elif ch == 3:
            serve()
        elif ch == 4:
            display()
        elif ch == 5:
            break
        else:
            print("Invalid Choice!")

main()