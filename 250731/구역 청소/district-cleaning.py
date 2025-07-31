a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
ans = 0
if b < c:
    if a > d:
        ans = abs(a - d)
else:
    ans = abs(b - c)


print(ans)


# print(ans)
