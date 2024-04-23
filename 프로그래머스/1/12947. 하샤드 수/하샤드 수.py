def solution(x):
    
    a = 0
    x = str(x)
    for i in range(len(x)):
        a += int(x[i])        
    
    x = int(x)
    if x % a == 0:
        answer = True
    else:
        answer = False
    return answer