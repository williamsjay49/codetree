inp = [list(map(int, input())) for _ in range(3)]

MAX_X = 3
MAX_A = 9
ans = 0
for i in range(1, MAX_A + 1):
    for j in range(i + 1, MAX_A + 1):
        win = False
        
        num_i = 0
        num_j = 0


        #for Horizontal
        for k in range(MAX_X):
            num_i = 0
            num_j = 0

            for l in range(MAX_X):
                if inp[k][l] == i:
                    num_i += 1
                if inp[k][l] == j:
                    num_j += 1
            
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

        #for Vertical
        for k in range(MAX_X):
            num_i = 0
            num_j = 0

            for l in range(MAX_X):
                if inp[l][k] == i:
                    num_i += 1
                if inp[l][k] == j:
                    num_j += 1
            
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

        #for Diagonal -> right
        num_i = 0
        num_j = 0
        for k in range(MAX_X):
            if inp[k][k] == i:
                num_i += 1
            if inp[k][k] == j:
                num_j += 1
        
        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
            win = True

        #for Diagonal -> left
        num_i = 0
        num_j = 0
        for k in range(MAX_X):
            if inp[k][MAX_X - k - 1] == i:
                num_i += 1
            if inp[k][MAX_X - k - 1] == j:
                num_j += 1
        
        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
            win = True

        if win:
            ans += 1

print(ans)


# ans = 0
# # Please write your code here.
# # print(inp)
# team = []
# pair = 0
# diag1 = [0] * 10
# diag2 = [0] * 10
# for l in range(3):
#     row = [0] * 10
#     col = [0] * 10
#     for m in range(3):
#         #Rows
#         row[inp[l][m]] += 1

#         #Columns
#         col[inp[m][l]] += 1
    
#         #Diagonal
#         if l == m:
#             diag1[inp[l][l]] += 1

#         if l == 2 - m:
#             diag2[inp[l][l]] += 1
    
#     # print(row)
#     # print(col)
#     # print(diag)
#     if max(row) == 2 and pair != (row.index(2), row.index(1)):
#         pair = (row.index(2), row.index(1))
#         team.append(pair)

#     if max(col) == 2 and pair != (col.index(2), col.index(1)):
#         pair = (col.index(2), col.index(1))
#         team.append(pair)
    
# if max(diag1) == 2 and pair != (diag1.index(2), diag1.index(1)):
#     pair = (diag1.index(2), diag1.index(1))
#     team.append(pair)

# if max(diag2) == 2 and pair != (diag2.index(2), diag2.index(1)):
#     pair = (diag2.index(2), diag2.index(1))
#     team.append(pair)



# print(len(team))
    
