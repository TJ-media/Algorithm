def next(n):
    num = list(str(n))

    i = len(num) - 2
    while i >= 0 and num[i] >= num[i+1]:
        i = i - 1

    j = len(num) - 1
    while j >= 0 and num[i] >= num[j]:
        j = j - 1
    
    num[i], num[j] = num[j], num[i]

    num = num[:i + 1] + sorted(num[i + 1:])

    return int(''.join(num))

print(next(input()))
