n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]
#가장 많은 터지는 폭탄, 여러개 경우에는 가장 큰 번호, 아무폭탄 터지지 않는 경우 -> 0

ans = 0
temp = 0
for i in range(n - k):
    cnt = 1
    for j in range(i + 1, i + k + 1):
        
        if num[i] == num[j]:
            cnt += 1
        # print(i, cnt)
        
    if cnt > ans:
        ans = cnt
        temp = num[i]
    
    elif cnt == ans and cnt != 0:
        temp = max(temp, num[i])


print(temp)
