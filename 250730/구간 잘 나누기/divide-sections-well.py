import sys
MAX_NUM = 10000

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = MAX_NUM
for i in range(1, MAX_NUM + 1):

    possible = True
    segment = 1
    cnt = 0
    
    for j in range(n):
        if a[j] > i:
            possible = False
            break

        if cnt + a[j] > i:
            cnt = 0
            segment += 1
        
        cnt += a[j]
            
    if possible and segment <= m:
        ans = min(ans, i)

        
print(ans)
        


































# for i in range(1, MAX_NUM + 1):
#     possible = True
#     section = 1
#     total = 0

#     for j in range(n):
#         if a[j] > i:
#             possible = False
#             break
#         if total + a[j] > i:
#             total = 0
#             section += 1
#         total += a[j]

#     if possible and section <= m:
#         print(i)
#         break
