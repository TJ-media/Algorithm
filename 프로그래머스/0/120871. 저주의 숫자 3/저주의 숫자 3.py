def solution(n):
    arr = []
    for i in range(1, 200):
        if i % 3 != 0 and '3' not in str(i):
                arr.append(i)
                   
    answer = arr[n-1]
    return answer