N = int(input())
seat = input()

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
ans = 0
start_idx = 0
for i in range(N):

    if seat[i] == "1":

        diff = i - start_idx
        ans = max(diff // 2, ans)

        start_idx = i

# print(start_idx)

diff = N - 1 - start_idx
ans = max(diff, ans)

print(ans)
