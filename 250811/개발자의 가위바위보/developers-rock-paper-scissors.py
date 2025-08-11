N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]


# Please write your code here.


player1, player2 = 0, 0
for x, y in moves:
    if x == y:
        continue

    if x == 1:
        if y == 2:
            player2 += 1
        
        else:
            player1 += 1

    if x == 2:
        if y == 1:
            player1 += 1
        
        else:
            player2 += 1

    if x == 3:
        if y == 1:
            player2 += 1

        else:
            player1 += 1

print(max(player1, player2))