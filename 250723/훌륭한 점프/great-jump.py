import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))
temp = sorted(arr)
# Please write your code here.
def max_res(val):
    coll = []
    for i, elem in enumerate(arr):
        if elem >= val or i == 0 or i == n - 1:
            coll.append(i)
    
    # print(coll, val)
    for i in range(1, len(coll)):
        # print(coll, val)
        if coll[i] - coll[i - 1 ] > k:
            return False

    return True

ans = sys.maxsize
for i in range(n):

    if max_res(arr[i]) and i != 0 and i != n - 1:
        temp, arr[i] = arr[i], 0
        # print(arr)
        ans = min(ans, max(arr))
        arr[i] = temp

print(ans)
