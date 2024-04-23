def solution(sides):
    
    a = sides[0]
    b = sides[1]
    answer = 0
    
    if a > b:
        for i in range(a-b+1, a+b, 1):
            answer += 1
    
    if b > a:
        for j in range(b-a+1, a+b, 1):
            answer += 1
    
    if a == b:
        for k in range(1, a+b, 1):
            answer += 1
            
    return answer