# import sys
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# temp = sorted(arr)
# # Please write your code here.
# def max_res(val):
#     coll = []
#     for i, elem in enumerate(arr):
#         if elem >= val or i == 0 or i == n - 1:
#             coll.append(i)
    
#     # print(coll, val)
#     for i in range(1, len(coll)):
        
#         if coll[i] - coll[i - 1 ] > k:
#             # print(coll, arr[i], arr[i - 1])
#             return False

#     return True

# ans = sys.maxsize
# for i in range(n):

#     if max_res(arr[i]) and i != 0 and i != n - 1:
#         temp, arr[i] = arr[i], 0
#         print(arr)
#         ans = min(ans, max(arr))
#         arr[i] = temp

# print(ans)

def isCan(index, n, k, arr):
    cnt = 0
    temp = [0] * 100
    for i in range(n):
        if arr[i] <= index:
            temp[cnt] = i
            cnt += 1
    
    for i in range(1, cnt):
        dis = temp[i] - temp[i - 1]
        if dis > k:
            return False
    return True

# Reading input in the specified format
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Initialize the answer with a large value
answer = 21 * 10**8

# Loop through possible minimum values starting from 100 down to the maximum of the first and last values
for i in range(100, max(arr[0], arr[n-1]) - 1, -1):
    if isCan(i, n, k, arr):
        answer = min(answer, i)

# Print the final result
print(answer)
