students = []

# Insert student details
def insert():
    n = int(input("Enter number of students: "))

    for i in range(n):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        cgpa = float(input("Enter CGPA: "))

        students.append([roll, name, cgpa])

# Selection Sort - Descending CGPA
def selection_sort():
    for i in range(len(students)):
        max = i

        for j in range(i + 1, len(students)):
            if students[j][2] > students[max][2]:
                max = j

        students[i], students[max] = students[max], students[i]

    print("Selection Sort Completed!")

# Insertion Sort and count shifts
def insertion_sort():
    shifts = 0

    for i in range(1, len(students)):
        key = students[i]
        j = i - 1

        while j >= 0 and students[j][2] < key[2]:
            students[j + 1] = students[j]
            shifts += 1
            j -= 1

        students[j + 1] = key

    print("Insertion Sort Completed!")
    print("Total Shifts:", shifts)

# Display top 5 students
def display():
    print("\nTop 5 Students:")
    for s in students[:5]:
        print("Roll No:", s[0], "Name:", s[1], "CGPA:", s[2])

# Main function
def main():
    insert()

    print("\n1. Selection Sort")
    print("2. Insertion Sort")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        selection_sort()
    elif ch == 2:
        insertion_sort()
    else:
        print("Invalid Choice!")
        return

    display()

main()