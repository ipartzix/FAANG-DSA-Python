# acending order
arr = [5,7,8,4,1,6,9,2]
n =len(arr)

def selection_sort(arr):
    for i in range(0 , n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index ] = arr[min_index],arr[i]
    print(arr)

selection_sort(arr)


arr = [5, 7, 8, 4, 1, 6, 9, 2]
n = len(arr)

# decending order 
def selection_sort(arr):
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


selection_sort(arr)
