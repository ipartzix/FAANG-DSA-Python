nums = [0,2,4,0,3,0,6,8]

def endZero(nums):
    n =len(nums)
    count = 0

    for i in range(n):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1

    while count < n:
        nums[count] = 0
        count += 1

    print(nums)

endZero(nums)

