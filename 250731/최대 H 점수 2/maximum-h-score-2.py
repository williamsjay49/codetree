
N, L = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
ans  = 0
for i in range(1, N + 1):
    cnt = 0
    cntl = 0

    for j in range(N):
        if a[j] >= i:
            cnt += 1
        
        elif a[j] == i - 1:
            if cntl < L:
                cntl += 1
                cnt += 1
    
    if cnt >= i:
        ans = i


print(ans)