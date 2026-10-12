num1 = [ 12 ,33,56,78,976,98345]
num2 = [1,56,8,3,2,5,75,3,22]

def checkSortedArray (arr):

    n = len(arr)
    for i in range(0,n-1):
        if arr[i]> arr[i+1]:
            return"Unsorted Array"

    return"Sorted Array"

print(checkSortedArray(num1))
print("=" * 30)
print(checkSortedArray(num2))
