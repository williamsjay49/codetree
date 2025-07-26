import sys
n = int(input())
adjacent = list(map(int, input().split()))
# Please write your code here.

arr = [0] * n
for i in range(1, n + 1):
    arr[0] = i

    for j in range(1, n):
        arr[j] = adjacent[j - 1] - arr[j - 1]

    # print(arr)

    satisfied = True
    exist = [False] * 1001
    for k in range(n):
        if arr[k] < 1 or arr[k] > n:
            satisfied = False

        else:

            if exist[arr[k]]:
                satisfied = False
        
            exist[arr[k]] = True

    if satisfied:
        for el in arr:
            print(el, end=" ")
        
        sys.exit()
        


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

# import sys

# MAX_N = 1000

# # 변수 선언 및 입력
# n = int(input())
# a = list(map(int, input().split()))
# arr = [0] * n

# # 모든 1 ~ n이 등장하는 수열의 개수는 n!개입니다.
# # 이를 완전탐색하기 위해서는 1000!개의 수열을 알아보아야 하며,
# # 이는 아무리 컴퓨터라 해도 너무 많은 경우의 수를 세야 합니다.
# # 따라서 보다 효율적인 방법을 찾아야 합니다.

# # 잘 생각해 보면, 수열의 첫 번째 수만 결정한다면
# # 그 뒤의 숫자들은 자동으로 값이 하나로 결정된다는 것을 알 수 있습니다.
# # 따라서 수열의 첫 번째 수를 기준으로 모든 수열을 탐색해 볼 수 있습니다.
# for i in range(1, n + 1):
#     # 수열의 첫 번째 수가 i일 때
#     arr[0] = i
    
#     for j in range(1, n):
#         # a[j - 1]는 arr[j] + arr[j - 1]의 값이기 때문에, 이 식을 잘 이용하면
#         # arr[0]에서 arr[1]을, arr[1]에서 arr[2]를 차근차근 알 수 있습니다.
#         arr[j] = a[j - 1] - arr[j - 1]
    
#     print("/")

#     # arr수열에 1부터 n까지의 값이 한 번씩 이용되는지 확인합니다.
#     # satisfied : arr수열에 1부터 n까지의 값이 한 번씩 이용될때 true
#     # exist : 한 번이라도 해당 숫자가 arr수열에 존재했다면 true
#     # 같은 숫자가 앞에 있었다면 exist배열을 확인했을 때 true가 나오게 됩니다.
#     satisfied = True
#     exist = [False] * (MAX_N + 1)
#     for j in range(n):
#         if arr[j] <= 0 or arr[j] > n:
#             satisfied = False
#         else:
#             if exist[arr[j]]:
#                 satisfied = False
#             exist[arr[j]] = True

#     if satisfied:
#         for j in range(n):
#             print(arr[j], end=" ")
#         sys.exit()
