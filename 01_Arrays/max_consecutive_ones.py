nums = [1, 1, 0, 1, 1, 1]

def maxConsecutive(nums):
    counter = 0
    max_counter = 0
    for i in nums:
        if i == 1:
            counter += 1
            max_counter = max(max_counter , counter)

        else:
            counter = 0  
    return max_counter 
        

print(maxConsecutive(nums))