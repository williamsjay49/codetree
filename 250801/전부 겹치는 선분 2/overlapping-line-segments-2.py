import sys
MAX_N = 100
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n) ]


not_possible = True
for i in range(n):
    cnt = 1
    x1, x2 = 0, sys.maxsize

    for j in range(n):
        if j == i:
            continue
            
        x1 = max(x1, arr[j][0])
        x2 = min(x2, arr[j][1])

        if x1 <= x2:
            cnt += 1

# print(cnt)
    if cnt == n - 1:
        not_possible = False


if not_possible:
    print("Yes")
else:
    print("No")