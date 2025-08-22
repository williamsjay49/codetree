n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = min(a)
ans = -1
diff = 101
NO_DUPLICATE = True

for i in range(n):
    if a[i] != min_val:

        if a[i] - min_val <= diff:
            ans = i + 1

            if diff == a[i] - min_val:
                NO_DUPLICATE = False
            
            else:
                NO_DUPLICATE = True
            
            diff = a[i] - min_val

         
    
if NO_DUPLICATE:
    print(ans)
else:
    print(-1)
        