def solution(s):
    
    a = list(s.split(' '))
    answer = 0
    
    for i in range(len(a)):
        if a[i] != 'Z':
            answer += int(a[i])
        else:
            answer -= int(a[i-1])
    
    return answer