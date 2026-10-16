# Merge 2 Sorted Arrays Without Duplicates
num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 7, 9]


def merge2arr(num1, num2):
    i = 0
    j = 0
    result = []

    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            if not result or result[-1] != num1[i]:
                result.append(num1[i])
            i += 1

        elif num1[i] > num2[j]:
            if not result or result[-1] != num2[j]:
                result.append(num2[j])
            j += 1

        else:
            if not result or result[-1] != num1[i]:
                result.append(num1[i])
            i += 1
            j += 1

    while i < len(num1):
        if not result or result[-1] != num1[i]:
            result.append(num1[i])
        i += 1

    while j < len(num2):
        if not result or result[-1] != num2[j]:
            result.append(num2[j])
        j += 1

    return result


print(merge2arr(num1, num2))