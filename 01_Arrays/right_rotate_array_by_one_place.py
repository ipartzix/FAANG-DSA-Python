nums = [5,-2,6,9,23,7,8,4]
arr = [3,5,6,7,34,6,23,2,4]

def oneRotated (nums):
    nums[:] = nums[-1:]+nums[0:-1] # nums[:] is used for inplace 
    print(nums)


oneRotated(nums)


def oneRotated2(arr):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0] = temp
    print(arr)

oneRotated2(arr)
