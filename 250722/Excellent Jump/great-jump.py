n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
def max_res(val):
    coll = []
    for i, elem in enumerate(arr):
        if elem >= val:
            coll.append(i)
    
    # print(coll)

    for i in range(1, len(coll)):
        if arr[i] - arr[i - 1 ] <= k:
            # print(coll)
            return max(coll)
    
    return -1

ans = 0
for i in range(1, max(arr) + 1):
    ans = max(ans, max_res(i))

print(ans)