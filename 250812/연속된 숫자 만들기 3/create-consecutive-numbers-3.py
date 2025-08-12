a = list(map(int, input().split()))

# Please write your code here.

if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
    print(0)
elif a[0] + 2 == a[1]:
    print(1)
elif a[0] + 3 == a[1]:
    print(2)
else:
    print(3)