n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

# def is_equal_arr(arr1, arr2):
#     # temp1 = sorted(arr1)
#     # temp2 = sorted(arr2)

#     if len(arr1) != len(arr2):
#         return False
    
#     for x, y in zip(arr1, arr2):
#         if x != y:
#             return False

#     return True

# def find(aa):
#     global temp

#     for j in range(1, n + 1):
#         for k in range(1, n + 1):
#             for l in range(1, n + 1):
#                 if j == k or j == l or k == l:
#                     continue
#                 # print(temp)

#                 if [j, k, l] == temp:
#                     continue

#                 if is_equal_arr([j + k, k + l], aa):
#                     temp = [j, k, l]
#                     return j, k, l
# ans = []
# temp = []
# for i in range(n - 2):

#     arr = [adjacent[i], adjacent[i + 1]]
#     j, k, l = find(arr)
#     # print(arr)
#     print(j, k, l, arr)
#     # if j not in ans:
#     #     ans.append(j)
#     # if k not in ans:
#     #     ans.append(k)
#     # if l not in ans:
#     #     ans.append(l)
                    

# print(ans)

# n = int(input())
# adjacent = list(map(int, input().split()))

for first in range(1, n + 1):
    answer = [0] * n
    used = [0] * (n + 1)
    answer[0] = first
    used[first] = 1
    valid = True

    for i in range(1, n):
        answer[i] = adjacent[i - 1] - answer[i - 1]
        if answer[i] < 1 or answer[i] > n or used[answer[i]]:
            valid = False
            break
        used[answer[i]] = 1

    if valid:
        print(' '.join(map(str, answer)))
        break
