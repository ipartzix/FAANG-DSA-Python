n = int(input("Enter the number to count :- "))
num = n
count = 0
while num > 0 :
    num % 10
    count += 1
    num = num // 10
print(count)