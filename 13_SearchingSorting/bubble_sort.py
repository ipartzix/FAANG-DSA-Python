num = [ 5,8,1,6,9,2,4]

arr = num

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2 , -1 ,-1):
        is_swap = False
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]

        if is_swap == False:
            break    
    print(arr)

bubble_sort(arr)