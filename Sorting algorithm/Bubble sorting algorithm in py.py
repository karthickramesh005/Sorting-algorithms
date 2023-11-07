# Bubble sorting algorithm in py :

def bubble(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0,n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
                swap = True

        if not swap :
            break
         
                

                


arr = list(map(int,input("Enter a array items : ").split()))
print("The unsorted array :",arr)
bubble(arr)
print("The Bubble sorted array : ",arr)
