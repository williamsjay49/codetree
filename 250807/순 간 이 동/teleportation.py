import sys
a, b, x, y = map(int, input().split())

# Please write your code here.

minVal = min(x, y)
maxVal = max(x, y)

if abs(a - b) < (abs(a - minVal) + abs(b - maxVal)):
    print(abs(a - b))

else:
    print(abs(a - minVal) + abs(b - maxVal))