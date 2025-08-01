N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.
ans = 100
arr = [-1] * (N + 1)
# EXIST = [False] * (N + 1)
move = 0
for i in range(1, N + 1):
    for j in range(N):
        if pigeon[j] != i:
            continue

        # EXIST[i] = True

        if arr[i] == -1:
            arr[i] = position[j]

        elif arr[i] != position[j]:
            arr[i] = position[j]
            move += 1


print(move)