num = [5, 8, 1, 6, 9, 2, 4]
arr = num

def insertion_sort(arr):
    n= len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>= 0 and arr[j]>key:
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)


insertion_sort(arr)