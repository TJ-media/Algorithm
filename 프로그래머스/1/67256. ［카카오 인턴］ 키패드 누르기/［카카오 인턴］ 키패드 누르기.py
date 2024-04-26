def solution(numbers, hand):
    distance = [
                [
                    [2, 0, 3],
                    [2, 1, 1],
                    [2, 2, 0],
                    [2, 3, 1],
                    [2, 4, 2],
                    [2, 5, 1],
                    [2, 6, 2],
                    [2, 7, 3],
                    [2, 8, 2],
                    [2, 9, 3],
                    [2, 10, 4],
                    [2, 11, 4]
                ],
                [
                    [5, 0, 2],
                    [5, 1, 2],
                    [5, 2, 1],
                    [5, 3, 2],
                    [5, 4, 1],
                    [5, 5, 0],
                    [5, 6, 1],
                    [5, 7, 2],
                    [5, 8, 1],
                    [5, 9, 2],
                    [5, 10, 3],
                    [5, 11, 3]
                ],
                [
                    [8, 0, 1],
                    [8, 1, 3],
                    [8, 2, 2],
                    [8, 3, 3],
                    [8, 4, 2],
                    [8, 5, 1],
                    [8, 6, 2],
                    [8, 7, 1],
                    [8, 8, 0],
                    [8, 9, 1],
                    [8, 10, 2],
                    [8, 11, 2],
                ],
                [
                    [0, 0, 0],
                    [0, 1, 4],
                    [0, 2, 3],
                    [0, 3, 4],
                    [0, 4, 3],
                    [0, 5, 2],
                    [0, 6, 3],
                    [0, 7, 2],
                    [0, 8, 1],
                    [0, 9, 2],
                    [0, 10, 1],
                    [0, 11, 1]
                ]   
               ]
    
    answer = ''
    lt = 10 # left thumb 10 == *
    rt = 11 # right thumb 11 == #
    for i in numbers:
        if i in [1, 4, 7]:
            lt = i
            answer += 'L'
        elif i in [3, 6, 9]:
            rt = i
            answer += 'R'
        elif i == 2:
            ld = distance[0][lt][2]
            rd = distance[0][rt][2]
            if ld < rd:
                lt = i
                answer += 'L'
            elif ld > rd:
                rt = i
                answer += 'R'
            else:
                if hand == 'left':
                    lt = i
                    answer += 'L'
                else:
                    rt = i
                    answer += 'R'
        elif i == 5:
            ld = distance[1][lt][2]
            rd = distance[1][rt][2]
            if ld < rd:
                lt = i
                answer += 'L'
            elif ld > rd:
                rt = i
                answer += 'R'
            else:
                if hand == 'left':
                    lt = i
                    answer += 'L'
                else:
                    rt = i
                    answer += 'R'
        elif i == 8:
            ld = distance[2][lt][2]
            rd = distance[2][rt][2]
            if ld < rd:
                lt = i
                answer += 'L'
            elif ld > rd:
                rt = i
                answer += 'R'
            else:
                if hand == 'left':
                    lt = i
                    answer += 'L'
                else:
                    rt = i
                    answer += 'R'
        elif i == 0:
            ld = distance[3][lt][2]
            rd = distance[3][rt][2]
            if ld < rd:
                lt = i
                answer += 'L'
            elif ld > rd:
                rt = i
                answer += 'R'
            else:
                if hand == 'left':
                    lt = i
                    answer += 'L'
                else:
                    rt = i
                    answer += 'R'

    return answer