import sys
n = int(input())
arr = list(input().split())

# Please write your code here.
matched = sorted(arr)
cnt = 0
dist = 0
i = 1
for i in range(1, n):
    # print(i)
    for j in range(i + 1, n):
        # print(arr[j], arr[i])
        if ord(arr[i]) - ord(arr[j]) >= 1:
            # print(arr[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1

        # print(arr)
        break
            

print(cnt)
