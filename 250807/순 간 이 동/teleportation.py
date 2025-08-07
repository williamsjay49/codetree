import sys
a, b, x, y = map(int, input().split())

# Please write your code here.

minVal = min(abs(a - x), abs(a - y))
maxVal = min(abs(b - x), abs(b - y))

if abs(a - b) < (minVal + maxVal):
    print(abs(a - b))

else:
    print(minVal + maxVal)

