MAX_N = 100
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n) ]


cnt = 0
x1, x2 = arr[0][0], arr[0][1]

for i in range(1, n):
    if x2 < arr[i][0] or arr[i][1] < x1:
        cnt += 1

# print(cnt)
if cnt == 1:
    print("Yes")
else:
    print("No")
