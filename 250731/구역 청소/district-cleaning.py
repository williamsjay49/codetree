a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
ans = 0
if b < c:
    print(abs(a - d))

else:
    print(abs(b - c))
