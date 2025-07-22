N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
ans__ = 0
for i in range(1, 10001):
    cnt = 0
        
    for el in arr:
        if i <= el <= K + i:
            cnt += 1

    ans__ = max(cnt, ans__)

print(ans__)
