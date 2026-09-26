n = 371
num = n
total = 0
digit_num = len(str(num))

while num > 0 :
    ld = num % 10
    total = total+(ld **digit_num)
    num = num // 10


if total == n:
    print("Amstrong number ")
else:
    print(" NOT Amstrong number ")
