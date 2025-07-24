N = int(input())
seat = list(input())

# Please write your code here.

def min_num():
    dist = N

    for i in range(N):
        for j in range(i + 1, N):
            if seat[i] == '1' and seat[j] == '1':
                dist = min(dist, j - i)

    return dist

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if seat[j] == '0' and seat[i] == '0':            
            seat[j] = seat[i] = '1'

            ans = max(ans, min_num())

            seat[j], seat[i] = '0'

print(ans)

