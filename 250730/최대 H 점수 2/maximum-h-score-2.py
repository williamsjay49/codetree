import sys
N, L = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
0 - 100, L


for i in range(100, -1, -1):
    for j in range(N):
        a[j] += L
        cnt = 0
        for k in range(N):
            if a[k] >= i:
                cnt += 1
        
        if cnt >= i:
            print(i)
            sys.exit()

        a[j] -= L
        
