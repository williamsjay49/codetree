n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]
#가장 많은 터지는 폭탄, 여러개 경우에는 가장 큰 번호, 아무폭탄 터지지 않는 경우 -> 0

ans = 0

for i in range(0, n - k + 1, k):
    arr = [0] * 1000001
    cnt = 0
    for j in range(i, i + k):
        arr[num[j]] += 1
ans = max(arr)
# print(ans)
temp = 0
if arr.count(ans) > 1:
    for i in range(1000000, -1, -1):
        if arr[i] == ans:

            temp = i
            break

else:
    temp = arr.index(ans)


print(temp)