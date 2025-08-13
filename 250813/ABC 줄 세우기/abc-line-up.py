n = int(input())
arr = list(input().split())

# Please write your code here.
last_cord = ord(arr[-1])
curr_idx = -1
cnt = 0

for i in range(n):

    for j in range(i + 1, n):
        if ord(arr[i]) + 1 == ord(arr[j]):
            if j - i != 1:
                arr[i + 1], arr[j] = arr[j], arr[i + 1]

                cnt += 1
            break

print(cnt)
        