def save():
    a = input().split()
    m = int(a[1])
    arr = list(map(int, input().split()))
    return m, arr

def cal(m, arr):
    for _ in range(m):
        b = input().split()
        i = int(b[0]) - 1
        j = int(b[1])
        k = int(b[2]) - 1

        arr_temp = arr[i:j]
        arr_temp = sorted(arr_temp)
        print(arr_temp[k])

m, arr = save()
cal(m, arr)
