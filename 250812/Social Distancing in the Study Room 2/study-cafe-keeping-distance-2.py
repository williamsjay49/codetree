N = int(input())
seats = list(input())

# Please write your code here.
max_dist = 0
max_i, max_j = -1, -1
for i in range(N):

    if seats[i] == '1':
        for j in range(i + 1, N):

            if seats[j] == '1':
                if j - i > max_dist:
                    max_dist = j - i

                    max_j, max_i = j, i

                break
        
    
seats[(max_j + max_i) // 2] = '1'
# print(seats, max_j, max_i)
ans = 1001
for i in range(N):
    if seats[i] == '1':
        for j in range(i + 1, N):
            if seats[j] == '1':
                ans = min(ans, j - i)
                break
                
if seats[0] == '0':
    for i in range(1, N):
        if seats[i] == '1':
            ans = max(ans, i)
            break

if seats[-1] == '0':
    for i in range(N-2, -1, -1):
        if seats[i] == '1':
            ans = max(ans, N-1 - i)
            break

print(ans)