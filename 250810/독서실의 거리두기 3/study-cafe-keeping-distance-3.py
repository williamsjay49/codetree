import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
seats = list(input())

# Step1. 최적의 위치 찾기
# 인접한 쌍들 중 가장 먼 1간의 쌍을 찾습니다.
max_dist = 0
max_i, max_j = -1, -1
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                # 1간의 쌍을 골랐을 때
                # 두 좌석간의 거리가 지금까지의 최적의 답 보다 더 좋다면
                # 값을 갱신해줍니다.
                if j - i > max_dist:
                    max_dist = j - i

                    # 이때, 두 좌석의 위치를 기억합니다.
                    max_i, max_j = i, j
                
                # 인접한 쌍을 찾았으므로 빠져나옵니다.
                break

# Step2. 최적의 위치에 1을 놓습니다.
# 가장 먼 쌍의 위치 가운데에 놓으면 됩니다.
seats[(max_i + max_j) // 2] = '1'

# Step3. 이제 인접한 쌍들 중 가장 가까운 1간의 쌍을 찾습니다.
# 이때의 값이 답이 됩니다.
ans = INT_MAX
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                ans = min(ans, j - i)

                # 인접한 쌍을 찾았으므로 빠져나옵니다.
                break

print(ans)



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


# def get_min():
#     min_num = int(2.1e9)
#     last_flag = -1
#     now_flag = -1
#     for i in range(n):
#         now = seats[i]
#         if now == '1':
#             now_flag = i
#         else:
#             now_flag = -1
#         if now_flag != -1:
#             if last_flag != -1:
#                 sub = now_flag - last_flag
#                 min_num = min(min_num, sub)
#             last_flag = now_flag
#     return min_num


# n = int(input())
# seats = list(input().strip())

# answer = -int(2.1e9)
# for i in range(n):
#     for j in range(i + 1, n):
#         if seats[i] == '1' or seats[j] == '1':
#             continue
#         seats[i] = '1'
#         seats[j] = '1'
#         answer = max(answer, get_min())
#         seats[i] = '0'   # reset
#         seats[j] = '0'   # reset

# print(answer)
