# n, k = map(int, input().split())
# num = [int(input()) for _ in range(n)]
# #가장 많은 터지는 폭탄, 여러개 경우에는 가장 큰 번호, 아무폭탄 터지지 않는 경우 -> 0

# ans = 0
# temp = 0
# for i in range(n - k + 1):
#     cnt = 1
#     for j in range(i + 1, i + k + 1):
        
#         if num[i] == num[j]:
#             cnt += 1
#         # print(i, cnt)
        
#     if cnt > ans:
#         ans = cnt
#         temp = num[i]
    
#     elif cnt == ans and cnt != 0:
#         temp = max(temp, num[i])


# print(temp)


from collections import Counter

n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]

ans = 0        # Highest explosion count
res = 0        # Bomb value with highest count

for i in range(n - k + 1):  # inclusive range for last window
    window = num[i:i + k + 1]
    count = Counter(window)
    max_cnt = max(count.values())
    
    # Find all bomb numbers that appear max_cnt times
    candidates = [val for val, c in count.items() if c == max_cnt]
    max_bomb = max(candidates)

    if max_cnt > ans:
        ans = max_cnt
        res = max_bomb
    elif max_cnt == ans:
        res = max(res, max_bomb)

# If the highest count is 1 (no explosion), return 0
print(res if ans > 1 else 0)
