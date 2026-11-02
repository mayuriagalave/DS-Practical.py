# Quick Sort Program

# Partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

# Main function
def main():
    n = int(input("Enter number of students: "))
    arr = []

    for i in range(n):
        marks = float(input("Enter percentage: "))
        arr.append(marks)

    quick_sort(arr, 0, n - 1)

    print("Sorted Percentages:", arr)

main()