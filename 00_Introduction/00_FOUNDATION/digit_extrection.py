n = int(input("enter the number to the digits: "))
num = n

print("Digits are:- ")
while 0 < num :
    last_digit = num % 10
    print(last_digit)
    num = num // 10