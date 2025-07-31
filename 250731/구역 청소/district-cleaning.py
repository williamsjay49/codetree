# a, b = map(int, input().split())
# c, d = map(int, input().split())

# # Please write your code here.
# ans = 0
# if b < c or d < a:
#     print(ans)

# else:
#     ans = abs(min(a, c) - max(d, b))
#     print(ans)


a, b = map(int, input().split())
c, d = map(int, input().split())

# Check if the intervals [a, b] and [c, d] overlap
if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
    print(max(a, b, c, d) - min(a, b, c, d))
else:
    print((b - a) + (d - c))
