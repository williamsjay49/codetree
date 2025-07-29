# n, k 입력
n, k = map(int, input().split())
# num_list 입력
num_list = list(map(int, input().split()))

# 함수들
# get_cost_from_bottom(num_to_add)
def get_cost_from_bottom(num_to_add):
    
    # curr_min_num
    curr_min_num = min_num + num_to_add

    # needed_cost
    needed_cost = 0

    # num_list를 돌면서
    for num in num_list:
        # curr_min_num보다 작은 값을 발견하면
        if num < curr_min_num:
            # 필요한 비용에 추가
            needed_cost += curr_min_num - num
    
    # 반환
    return needed_cost

# get_cost_from_top(num_to_minus)
def get_cost_from_top(num_to_minus):
    
    # curr_max_num
    curr_max_num = max_num - num_to_minus

    # needed_cost
    needed_cost = 0

    # num_list를 돌면서
    for num in num_list:
        # curr_max_num보다 큰 값을 발견하면
        if num > curr_max_num:
            # 필요한 비용에 추가
            needed_cost += num - curr_max_num
    
    # 반환
    return needed_cost

# 설계
# max_num, min_num
max_num, min_num = max(num_list), min(num_list)

# diff_need_to_be_modified
diff_need_to_be_modified = (max_num - min_num) - k

# low_cost
import sys
low_cost = sys.maxsize

# 완전 탐색 시작
for i in range(diff_need_to_be_modified + 1):
    # curr_cost
    curr_cost = get_cost_from_bottom(i) + get_cost_from_top(diff_need_to_be_modified - i)
    # low_cost update
    low_cost = min(low_cost, curr_cost)

# 출력
print(low_cost)