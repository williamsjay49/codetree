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

n=int(input())
ab=[
    tuple(map(int,input().split()))
    for _ in range (n)
]

def in_range(x):
    for i in range(n):
        if ab[i][0] <= 2**(i+1)*x and 2**(i+1)*x <= ab[i][1]:
            continue
        else:
            return False
    return True

ans=[]

for x in range(1,1000):
    if in_range(x):
        ans.append(x)

print(min(ans))

