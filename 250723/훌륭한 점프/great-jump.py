import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
def max_res(val):
    coll = []
    for i, elem in enumerate(arr):
        if elem <= val:
            coll.append(i)
    

    for i in range(1, len(coll)):
        # print(coll, val)
        if coll[i] - coll[i - 1 ] > k:
            return False
    
    return True

ans = sys.maxsize
for i in range(max(arr), min(arr) + 1, -1):

    if max_res(i):
        # print(i)
        ans = min(ans, i)

print(ans)