# N = int(input())
# seats = input()

# # Please write your code here.
# idx = 0
# dist = 0
# start = 0
# for i in range(1, N):

#     Found = True
#     if int(seats[i]) == 1:
#         idx = i
#         dist = (idx - start) // 2
#         # print(dist, idx)
#         for j in range(idx + 1, N):
#             if int(seats[j]) == 1 and (j - idx) < dist:
#                 start = i
#                 i = idx + 1

#                 # print(start, i)
#                 False
#                 break
        
#             idx = j
#         if Found:
#             print(dist)
#             break


def get_min():
    min_num = int(2.1e9)
    last_flag = -1
    now_flag = -1
    for i in range(n):
        now = seats[i]
        if now == '1':
            now_flag = i
        else:
            now_flag = -1
        if now_flag != -1:
            if last_flag != -1:
                sub = now_flag - last_flag
                min_num = min(min_num, sub)
            last_flag = now_flag
    return min_num


n = int(input())
seats = list(input().strip())

answer = -int(2.1e9)
for i in range(n):
    for j in range(i + 1, n):
        if seats[i] == '1' or seats[j] == '1':
            continue
        seats[i] = '1'
        seats[j] = '1'
        answer = max(answer, get_min())
        seats[i] = '0'   # reset
        seats[j] = '0'   # reset

print(answer)
