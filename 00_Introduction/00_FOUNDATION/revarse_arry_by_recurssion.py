arr = [5 , 7 ,3 , 2 ,6 ,1 ,5, 9]

# sm = []
# for i in range(len(num)-1 , -1 , -1):
#     sm.append(num[i])
# print(sm)

def func(arr , left ,right ):
    if left >= right :
        return
    arr[left],arr[right]=arr[right],arr[left]
    func(arr, left+1, right-1)

func(arr, 0, len(arr) - 1)
print(arr)
