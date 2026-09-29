"""
def greet():
    print("Infinite Recursion")
    greet()

greet()

# python has default depth 987 then it give error
# RecursionError: maximum recursion depth exceeded


"""
cnt = 0


def cunt():
    global cnt

    if cnt == 4:
        return

    print("paro")
    cnt += 1
    cunt()

cunt()
