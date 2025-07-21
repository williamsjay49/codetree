n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.


    
for i in range(1, 10000):
    is_avail = True
    cnt = 0
    arr = [0] * n
    for k in range(n):
        for j in range(i, 10000):
            if j != i and j % prev != 0:
                continue

            if ranges[k][0] <= j <= ranges[k][1]:
                arr[k] = 1
                break

            prev = j
    if 0 not in arr:
        print(i)
        break




