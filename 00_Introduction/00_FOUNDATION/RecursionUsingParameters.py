def func(n): # n is the time of print
    if n == 0:
        return 
    func(n-1)
    print(n)
    

func(5)