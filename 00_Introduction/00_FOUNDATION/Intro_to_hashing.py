"""
Hashinng 
"""

"""
 brout force method 
"""
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

# for num in m:
#     count = 0

#     for x in n :
#         if x == num:
#             count += 1
#     print(count)

# Time complexity O(m*n)

"""
Optimized method 
"""

# step 1:- create a list 

hash_list = [0]* 11
for num in n:
    hash_list[num] += 1

for num in m:
    if num > 10 or num <1:
        print(0)
    else:
        print(hash_list[num])