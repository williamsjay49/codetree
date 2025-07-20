N = int(input())
seat = list(input())

# diff = 0
# start_idx = 0

# for i in range(N):
#     if seat[i] == '1':  # Seat is occupied
#         # Calculate the segment length
#         diff = max(diff, (i - start_idx) // 2)
#         # print(i, start_idx)
#         # Update start index to the next position after the '1'
#         start_idx = i

# # After loop, check the last segment
# # print(start_idx)
# diff = max(diff, N - 1 - start_idx)

# print(diff)

def min_num():
    dist = N

    for i in range(N):
        for j in range(i + 1, N):
            if seat[i] == '1' and seat[j] == '1':
                dist = min(dist, j - i)

    return dist
ans = 0
for i in range(N):

    if seat[i] == '0':
        seat[i] = '1'

        ans = max(ans, min_num())

        seat[i] = '0'

print(ans)