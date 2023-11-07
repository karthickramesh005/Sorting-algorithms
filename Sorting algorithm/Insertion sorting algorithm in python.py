# Insertion sorting algorithm in python :


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

try:
    n = int(input("Enter the number of elements in the array: "))
    if n <= 0:
        print("Please enter a positive integer for the number of elements.")
    else:
        arr = list(map(int, input("Enter the elements separated by space: ").split()))
        
        insertion_sort(arr)
        
        print("Sorted array:", arr)
except ValueError:
    print("Invalid input. Please enter valid integers for the array elements.")
