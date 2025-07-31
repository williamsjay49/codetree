a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
ans = 0
if b < c or d < a:
    print(ans)

else:
    ans = abs(min(a, c) - max(d, b))
    print(ans)


# print(ans)
