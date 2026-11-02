nums = [1,0,-1,0,-2,2] 
target = 0

# brute force
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
                hash_set.add(nums[k])
    return list(my_set)


# optimal solution


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return ans
