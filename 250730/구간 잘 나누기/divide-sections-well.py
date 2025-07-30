import sys
MAX_NUM = 10000

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, 10):
    cnt = 0
    
    sub_total = 0
    maxval = 0
    for j in range(n):
        if j == 0 and a[j] > i:
            break

        sub_total += a[j]
        # print((sub_total, a[j], i, cnt),  end=" ")
        if sub_total > i:
            cnt += 1
            # ans = max(sub_total, ans)
            sub_total = 0
        
        else:
            maxval = max(sub_total, maxval)
            
    # print(maxval, cnt, i)
    # print()
    if cnt == (m - 1) and maxval == i:
        # ans = min(i, ans)
        ans = max(maxval, ans)
        # break
    

        
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
