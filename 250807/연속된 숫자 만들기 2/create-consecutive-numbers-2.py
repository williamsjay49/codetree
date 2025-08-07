pos = list(map(int, input().split()))

# Please write your code here.

count = 0

mid = pos[1]
if mid - pos[0] != 1 and pos[0] < pos[2]:
    pos[0], pos[1] = pos[1], pos[2] - 1

    mid = pos[2]

    count += 1

    if mid - pos[0] != 1:
        pos[2], pos[1] = pos[1], pos[0] + 1
        count += 1
elif pos[2] - mid != 1:
    pos[1], pos[2] = pos[0] + 1, mid
    count = 1


print(count)