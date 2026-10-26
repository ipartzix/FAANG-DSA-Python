"""
5   20  28
27  16  1
9   33  18
2D array
"""
# arr = [[5, 20, 28], [27, 26, 1], [9, 33, 18]]

arr =[
    [5 , 20 ,28],
    [27, 26 , 1],
    [9 , 33 ,18]
    ]

print(arr)
row = len(arr)
columns = len(arr[0])


for i in range(0,row):
    for j in range(0 ,columns):
        print(arr[i][j], end=" ")
    print()

print("_" * 30)
# upper triangonal

for i in range(0, row):
    for j in range(0, columns):
        if j >= i:
            print(arr[i][j], end=" ")
        else:
            print("#", end=" ")
    print()

print("_0" * 30)
# lower triangonal

for i in range(0 ,row):
    for j in range(0 , columns):
        if i >= j:
            print(arr[i][j], end=" ")
        else:
            print("$" , end=" ")
    print()
