"""

def greet():
    print("Infinite Recursion")
    greet()

greet()

# python has default depth 987 then it give error
# RecursionError: maximum recursion depth exceeded


"""
