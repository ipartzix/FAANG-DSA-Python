nums = [1,0,-1,0,-2,2] 
target = 0

#brute force
def fourSum(nums , target):
    n = len(nums)
    my_set = set()

    for i in range(0,n):
        for j in range(i+1 , n):
            for k in range(j+1 , n):
                for l in range(k+1 , n):
                    total = nums[i]+ nums[j]+ nums[k]+nums[l]
                    if total == target:
                        temp = [ nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
    return list(my_set)

print(fourSum(nums,0))

# better solution 

def foursum(nums , target):
    n = len(nums)
    my_set = set()

    for i in range(0 , n):
        for j in range(i+1 ,n):
            hash_set = set()
            for k in range(j+1 ,n):
                fourthEle = target -(nums[i]+ nums[j]+ nums[k])
                if fourthEle in hash_set:
                    temp = [ nums[i],nums[j],nums[k], fourthEle ]
                    temp.sort()
                    my_set.add(tuple(temp))
                my_set.add(nums[k])
    return list(my_set)