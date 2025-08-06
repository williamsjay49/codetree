import sys
a, b, x, y = map(int, input().split())

# Please write your code here.

dist = sys.maxsize

dist = min(dist, abs(a - y) + abs(x - b))
dist = min(dist, abs(a - y) + b)
dist = min(dist, abs(a - x) + abs(b - y))
dist = min(dist, abs(b - a))


print(dist)