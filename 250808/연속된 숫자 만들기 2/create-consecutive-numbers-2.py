pos = list(map(int, input().split()))
# Please write your code here.

pos.sort()

# Case 1: All three numbers are consecutive
if pos[0] + 1 == pos[1] and pos[1] + 1 == pos[2]:
    print(0)
# Case 2: Two numbers have a difference of exactly 2
elif pos[0] + 2 == pos[1] or pos[1] + 2 == pos[2]:
    print(1)
# Case 3: Otherwise, it always takes 2 moves
else:
    print(2)
