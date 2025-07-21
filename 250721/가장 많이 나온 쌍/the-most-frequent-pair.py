n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
ans = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        matched = 0

        for x, y in pairs:
            if i == x and j == y or y == i and x == j:
                # print(i, j)
                matched += 1
    
        ans = max(ans, matched)

print(ans)