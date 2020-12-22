def partition(arr, low, high):
    i  = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j]<= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[high] = arr[high] ,arr[i+1]
    return (i+1)

def quickSort(arr, low, high,level):
    
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        print(pi,arr, low, high,level)
        quickSort(arr, low, pi-1,"first")
        quickSort(arr, pi+1, high, "second")
arr = [2,3,5,1,7,6]
n = len(arr)
quickSort(arr, 0, n-1,"root")
print(arr)