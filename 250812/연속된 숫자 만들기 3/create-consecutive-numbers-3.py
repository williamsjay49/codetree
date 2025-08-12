a = list(map(int, input().split()))

# Please write your code here.

if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
    print(0)
else:
    ans = (a[1] - 1) - a[0]
    print(ans)