"""
Hashinng 
"""

"""
 brout force method 
"""
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

for num in m:
    count = 0

    for x in n :
        if x == num:
            count += 1
    print(count)

# Time complexity O(m*n)

"""
Optimized method 
"""
"""
Using List
"""
hash_list = [0]* 11
for num in n:
    hash_list[num] += 1

for num in m:
    if num > 10 or num <1:
        print(0)
    else:
        print(hash_list[num])

"""
Using Dictionary 
"""
dict_hash = {}

ran = len(n)
for i in range(0,ran):
    dict_hash[n[i]] = dict_hash.get(n[i],0)+1
print(dict_hash)

print("_______________________________________")
for num in m:
    if num > 10 or num < 1:
        print(0)
    else:
        print(dict_hash.get(num, 0))

# Time complexity is O(m+n)
