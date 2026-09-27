"""
for making dictionary we have 2 option
1st :- dictionary = dict()
2nd :- dictionary = {}
"""
num = [5,6,7,7,1,9,111,1,1,5,1,1]
freq_map = { }
for i in range(0, len(num)):
    if num[i] in freq_map :
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1
print(freq_map[1])


# Method 2
print("_________________________________")
nums = [1,3,5,4,2,3,7,1,1,2,4,8,7,5,1,7]
freq = {}

n = len(nums)

for i in range(0, n):
  freq[nums[i]] = freq.get(nums[i],0)+1

print(freq)