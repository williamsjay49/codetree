# n 입력
n = int(input())
# hills 입력
hills = [
    int(input())
    for _ in range(n)
]

# 함수들
# get_cost(to_add, to_minus)
def get_cost(to_add, to_minus):
    
    # new_lowest_hill, new_highest_hill
    new_lowest_hill, new_highest_hill = lowest_hill + to_add, highest_hill - to_minus

    # curr_cost
    curr_cost = 0

    # 모든 new_lowest_hill미만 높이의 hill을 
    # new_lowest_hill로 만드는 비용 계산
    for hill in hills:
        if hill < new_lowest_hill:
            curr_cost += (new_lowest_hill - hill) * (new_lowest_hill - hill)
    
    # 모든 new_highest_hill초과 높이의 hill을
    # new_highest_hill로 만드는 비용 계산
    for hill in hills:
        if hill > new_highest_hill:
            curr_cost += (hill - new_highest_hill) * (hill - new_highest_hill)
    
    # 반환
    return curr_cost

# 설계
# highest_hill, lowest_hill
highest_hill, lowest_hill = max(hills), min(hills)

# heights_to_be_adjust
heights_to_be_adjust = highest_hill - lowest_hill - 17

# lowest_cost
import sys
lowest_cost = sys.maxsize

# 완전 탐색 시작
for i in range(heights_to_be_adjust + 1):
    # lowest_cost update
    lowest_cost = min(lowest_cost, get_cost(i, heights_to_be_adjust - i))

# 출력
print(lowest_cost)