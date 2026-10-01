

def func (sum , i , n):
    if i > n:
        print(f"The sum is :{sum}")
        return
    func(sum+i , i+1 ,n)

func(0 , 1, 4)