n = 10
board = [input() for _ in range(n)]

# Please write your code here.

for i in range(n):
    for j in range(n):
        if board[i][j] == "L":
            l_x = i
            l_y = j
        
        if board[i][j] == "B":
            b_x = i
            b_y = j
        
        if board[i][j] == "R":
            r_x = i
            r_y = j


if l_x != b_x and l_y != b_y:
    print(abs(l_x - b_x) + abs(l_y - b_y) - 1)

elif l_x == b_x:
    if l_x == r_x and r_y > min(l_y, b_y) and r_y < max(l_y, b_y):
        print(abs(l_y - b_y) + 1)
    
    else:
        print(abs(l_y - b_y) - 1)


elif l_y == b_y:
    if l_y == r_y and r_x > min(l_x, b_x) and r_x < max(l_x, b_x):
        print(abs(l_x - b_x) + 1)
    
    else:
        print(abs(l_y - l_y ) - 1)