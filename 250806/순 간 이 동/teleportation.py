a, b, x, y = map(int, input().split())

# Please write your code here.

dist = 1001

dist = min(dist, abs(a - y) + abs(x - b))
dist = min(dist, abs(a - b) + abs(x - y))


print(dist)