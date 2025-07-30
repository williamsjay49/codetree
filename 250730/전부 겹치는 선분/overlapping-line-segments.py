n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

lst = [0] * 101

for i in range(n):
    start = x1[i]
    end = x2[i]
    for j in range(start, end + 1):
        lst[j] += 1

res = any(count >= n - 1 for count in lst)

print("Yes" if res else "No")
