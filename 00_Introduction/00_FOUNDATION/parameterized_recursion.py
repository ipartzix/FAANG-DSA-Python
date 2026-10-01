def func (sum , i , n):
    if i > n:
        print(f"The sum is :{sum}")
        return
    func(sum+i , i+1 ,n)

func(0 , 1, 4)

print("________")

def func_sum(n):
    if n == 1:
        return 1
    return n + func_sum(n - 1)

print(func_sum(10))
