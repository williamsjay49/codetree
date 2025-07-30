INT_MAX = float('inf')
MAX_N = 100

n = int(input())
x1 = []
x2 = []

# 입력
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

ans = False

# 모든 선분을 한 번씩 제외해 보고, 남은 선분들 사이에 공통 구간이 존재하는지 확인
for skip in range(n):
    max_x1 = 0
    min_x2 = INT_MAX

    for i in range(n):
        if i == skip:
            continue
        max_x1 = max(max_x1, x1[i])
        min_x2 = min(min_x2, x2[i])

    if min_x2 >= max_x1:
        ans = True
        break  # 한 번이라도 가능하면 더 확인할 필요 없음

print("Yes" if ans else "No")
