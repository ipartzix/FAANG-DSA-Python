"""
Brute Force solution

"""
num1 = 20

result1 =[]
for i in range(1,num1+1):
    if num1 % i == 0:
        result1.append(i)
print(result1)

print("______________________________")
"""
Better solution

"""

num2 = 12

result2 = []
for i in range(1, (num2 // 2)+1):
    if num2 % i == 0:
        result2.append(i)
result2.append(num2)
print(result2)

print("_____________________________________")
"""
Optimal Solution 

"""

from math import sqrt
num3 = 36
result3 = [] 
for i in range(1, int(sqrt(num3))+1 ):
    if num3 % i == 0:
        result3.append(i)
    if num3 // i != i :
        result3.append(num3//i)

result3.sort()
print(result3)
