def drugnum(num):
    a = 0
    if num == 1:
        return 1
    else:
        for i in range(1, num//2 + 1):
            if num % i == 0 and i ** 2 != num:
                a += 2
            elif i ** 2 == num:
                a += 1
            else:
                continue
    return a

def solution(left, right):
    answer = 0
    for j in range(left, right + 1):
        if drugnum(j) % 2 == 0:
            answer += j
        else:
            answer -= j
    return answer