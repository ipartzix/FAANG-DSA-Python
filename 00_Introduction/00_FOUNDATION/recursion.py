"""
def greet():
    print("Infinite Recursion")
    greet()

greet()

# python has default depth 987 then it give error
# RecursionError: maximum recursion depth exceeded


"""
cnt = 0

# Tail Recursion 
def cunt():
    global cnt
    if cnt == 4:
        return
    cnt += 1
    print("paro")
    cunt()
cunt()

# Head Recursion 
def cunt2():
    global cnt
    if cnt == 4:
        return
    cnt += 1
    cunt2()
    print("paro2")    
cunt2()