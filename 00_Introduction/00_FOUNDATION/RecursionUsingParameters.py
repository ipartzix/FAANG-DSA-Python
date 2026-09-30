def func(n): # n is the time of print
    if n == 0:
        return 
    func(n-1)
    print(n)
    

func(5)

print("_______________________")

def nnum(i ,n):
    if i > n:
        return
    print(i)
    nnum(i+1,n)

nnum(1,4)