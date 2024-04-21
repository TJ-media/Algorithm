def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    lux, luy, rdx, rdy = -1, -1, -1, -1

    # lux 찾기
    for i in range(n):
        if '#' in wallpaper[i]:
            lux = i
            break

    # luy 찾기
    for j in range(m):
        for k in range(n):
            if wallpaper[k][j] == '#':
                luy = j
                break
        if luy != -1:
            break

    # rdx 찾기
    for l in range(-1, -n-1, -1):
        if '#' in wallpaper[l]:
            rdx = n+l+1
            break

    # rdy 찾기
    for o in range(-1, -m-1, -1):
        for p in range(-1, -n-1, -1):
            if wallpaper[p][o] == '#':
                rdy = m+o+1
                break
        if rdy != -1:
            break

    answer = [lux, luy, rdx, rdy]
    return answer
