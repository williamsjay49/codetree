# N = int(input())
# seat = list(input())

# # Please write your code here.

# def min_num():
#     dist = N + 2

#     for i in range(N):
#         for j in range(i + 1, N):
#             if seat[i] == '1' and seat[j] == '1':
#                 dist = min(dist, j - i)

#     return dist
# ans = 0
# for i in range(N):
#     if seat[i] != '0':
#         continue
        
#     seat[i] = '1'

#     for j in range(i + 1, N):
#         if seat[j] != '0':
#             continue
            
#         seat[j] = '1'

#         ans = max(ans, min_num())

#         seat[j] = '0'
#         seat[i] = '0'

# print(ans)
N = int(input())
seat = list(map(int, input().strip()))

max_g = 0

for i in range(N):
    if seat[i] == 1:
        continue
    for j in range(N):
        if seat[j] == 1 or j == i:
            continue
        
        seat[i] = 1
        seat[j] = 1
        
        min_g = N + 2
        for k in range(N):
            if seat[k] == 1:
                for l in range(k + 1, N):
                    if seat[l] == 1:
                        min_g = min(min_g, l - k)
                        break

        max_g = max(max_g, min_g)
        seat[i] = 0
        seat[j] = 0

print(max_g)
