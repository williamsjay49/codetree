n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# def cont_sum(new_idx, cnt):
#     if cnt == 1:
#         return arr[new_idx], arr[new_idx]
    
#     cnt -= 1
#     new_idx, val = cont_sum(new_idx, cnt)
#     tot = val + arr[new_idx]
#     # print(new_idx, arr[new_idx])

#     return arr[new_idx], tot

# ans = 0
# for i in range(1, n + 1):
#     _, cur_sum = cont_sum(i, m)

#     ans = max(cur_sum, ans)

# print(ans)
    
ans = 0
for i in range(1, n + 1):
    tot = 0
    a = i
    for j in range(m):
        tot += arr[a]
        a = arr[a]


    ans = max(ans, tot)

print(ans)