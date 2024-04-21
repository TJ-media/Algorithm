def solution(cards):
    
    index = 0
    num_of_set = []
    _set = 0
    visited = [False] * len(cards)
    
    while not all(visited):
        
        if not visited[index]:
        
            current = index
            while not visited[current]:
                next_index = cards[current] - 1
                visited[current] = True
                current = next_index
                _set = _set + 1

            num_of_set.append(_set)
            _set = 0
        
        while index < len(cards) and visited[index]:
            index += 1
    
    num_of_set.sort()
    if len(num_of_set) < 2:
        answer = 0
    else:
        answer = num_of_set[-1]*num_of_set[-2]
    
    return answer