# import sys
# n = int(input())
# arr = list(input().split())

# # Please write your code here.
# matched = sorted(arr)
# cnt = 0
# dist = 0
# i = 1
# if arr == matched:
#     print(cnt)
#     sys.exit()

# while arr != matched:
#     for i in range(1, n):
#         # print(i)
#         for j in range(i + 1, n):
#             # print(arr[j], arr[i])
#             if ord(arr[i]) - ord(arr[j]) >= 1:
#                 # print(arr[i], arr[j])
#                 arr[i], arr[j] = arr[j], arr[i]
#                 cnt += 1

#             # print(arr)
#             break
            

# print(cnt)


from sys import stdin
n = int(stdin.readline())
base = stdin.readline().split()

cnt = 0

#Insertion sort algorithm would be efficient
for i in range(1, n): #increase range
    for j in range(i, 0, -1): #check range, from i to 1
        if ord(base[j-1]) > ord(base[j]): #smaller one goes forward
            base[j-1], base[j] = base[j], base[j-1]
            cnt += 1
        else:
            break
# print(base)
print(cnt)
