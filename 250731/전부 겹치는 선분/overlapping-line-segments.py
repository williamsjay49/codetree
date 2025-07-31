MAX_N = 100
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n) ]

# print(arr)
ans = 0
for i in range(1, 101):
    cnt = 0
    for x1, x2 in arr:
       
        # print(x1, x2)
        if x1 <= i <= x2:
            cnt += 1
    

    ans = max(ans, cnt)


if ans == n:
    print("Yes")
else:
    print("No")