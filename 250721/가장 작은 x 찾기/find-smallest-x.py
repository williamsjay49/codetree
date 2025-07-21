# n = int(input())
# ranges = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.


# for j in range(1, 10000):

#     cnt = 0
#     cur = j
#     for a, b in ranges:
#         exist = False
#         while True:
#             if a <= cur <= b:
#                 # print(cur, a, b, cnt)
#                 cur *= 2
#                 exist = True
#             else:
#                 break
        
#         if exist:
#             cnt += 1
#     if cnt == n: 
#         print(j)

#         break

# n=int(input())
# ab=[
#     tuple(map(int,input().split()))
#     for _ in range (n)
# ]

# def in_range(x):
#     for i in range(n):
#         if ab[i][0] <= 2**(i+1)*x and 2**(i+1)*x <= ab[i][1]:
#             continue
#         else:
#             return False
#     return True

# ans=[]

# for x in range(1,1000):
#     if in_range(x):
#         ans.append(x)

# print(min(ans))

n = int(input())
if not 1 <= n <= 10:
    print("Invalid N")
    exit()

ab = [tuple(map(int, input().split())) for _ in range(n)]
for a, b in ab:
    if not (1 <= a <= b <= 10000):
        print("Invalid range")
        exit()

def in_range(x):
    for i in range(n):
        min_val = ab[i][0] / (2 ** (i + 1))
        max_val = ab[i][1] / (2 ** (i + 1))
        if not (min_val <= x <= max_val):
            return False
    return True

ans = []
for x in range(1, 10001):  # Limit to reasonable range based on constraints
    if in_range(x):
        ans.append(x)
        break  # Stop at the first valid x to optimize

print(min(ans) if ans else -1)