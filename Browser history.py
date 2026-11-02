stack = []

# Visit a new page
def visit():
    url = input("Enter URL: ")
    stack.append(url)
    print("Page visited successfully!")

# Go back to previous page
def back():
    if len(stack) == 0:
        print("No previous page!")
    else:
        stack.pop()
        print("Went back to previous page!")

# Display current page
def current():
    if len(stack) == 0:
        print("No page opened!")
    else:
        print("Current Page:", stack[-1])

# Display browsing history
def history():
    print("Browsing History:", stack)

# Main function
def main():
    while True:
        print("\n1. Visit New Page")
        print("2. Go Back")
        print("3. Current Page")
        print("4. Show History")
        print("5. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            visit()
        elif ch == 2:
            back()
        elif ch == 3:
            current()
        elif ch == 4:
            history()
        elif ch == 5:
            break
        else:
            print("Invalid Choice!")

main()