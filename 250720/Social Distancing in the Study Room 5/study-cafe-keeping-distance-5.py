from sys import stdin
n = int(stdin.readline())
base = stdin.readline().strip()

ans = 0
for i in range(n): #position selection
    if base[i] == '1': #user exists
        continue
    tmp = float("inf")
    check = True
    for j in range(n):
        if check and (i == j or base[j] == '1'): #skip the first 1
            cnt = 1
            check = False
            continue
        elif check: #still haven't encountered 1, so skip
            continue
        if i == j or base[j] == '1': #calculate distance when encountering 1 afterwards
            # print(tmp)
            tmp = min(tmp, cnt)
            cnt = 1
        else:
            cnt += 1
    # print(i, j, tmp, cnt)
    ans = max(ans, tmp)
print(ans)
