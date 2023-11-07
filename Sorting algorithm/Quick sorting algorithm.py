# Quick sorting algorithm :
'''def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)'''

# Example usage:
arr =list(map(int,input("Enter a array elements : ").split()))
#sorted_arr = quicksort(arr)
#print("Sorted array:", sorted_arr)
print(sorted(arr))
