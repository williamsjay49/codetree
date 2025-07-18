N = int(input())
str = input()
arr = [0] * 91
# Please write your code here.

for i in range(N):
    for j in range(65, 91):
        if ord(str[i]) != j:
            continue
        
        arr[j] += 1

ans = 0
for el in str:
    stop = False

    
    convEl = ord(el)
    if arr[convEl] > 1:
        ans += 1
    
    else:
        stop = True
        ans += 1

    # print(ans)
    if stop:
        break

print(ans)