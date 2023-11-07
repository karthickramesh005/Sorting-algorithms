# Selection sorting algorithm :

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

try:
    n = int(input("Enter the number of elements in the array: "))
    if n <= 0:
        print("Please enter a positive integer for the number of elements.")
    else:
        arr = list(map(int, input("Enter the elements separated by space: ").split()))
        
        selection_sort(arr)
        
        print("Sorted array:", arr)
except ValueError:
    print("Invalid input. Please enter valid integers for the array elements.")
