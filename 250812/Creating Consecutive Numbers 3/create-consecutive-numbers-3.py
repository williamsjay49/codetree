a = list(map(int, input().split()))

# Please write your code here.

if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
    ans = 0

elif a[1] - a[0] < a[2] - a[1]:
    ans = a[2] - a[1] - 1

else:
    
    ans = a[1] - a[0] - 1

print(ans) 