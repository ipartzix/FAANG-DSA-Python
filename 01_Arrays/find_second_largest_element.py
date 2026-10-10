# Find the 2nd largest element in the array 
# general approch 
arr = [12,33,5,3,4,34,88,99,50]
lrg = arr[0]
sec_lrg =arr[0]

for i in arr:
    if i > lrg:
        lrg= i
for i in arr:
    if i> sec_lrg and i != lrg:
        sec_lrg= i
print(f"sec largest is :- {sec_lrg}")