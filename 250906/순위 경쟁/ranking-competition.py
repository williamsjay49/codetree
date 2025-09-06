n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
score = [0, 0, 0]
pos = ["A", "B", "C"]
total = 0
ans = 0
for i in range(n):
    cnt = 0
    idx = pos.index(c[i])
    score[idx] += s[i]

    top = max(score)

    for elem in score:
        if elem == top:
            cnt += 1
    
    if cnt != total:
        ans += 1
        total = cnt

print(ans)

#1 명 1 위 ~ A, B, C
#2 명 1 위 ~ AB, AC, BC
#3 명 1 위 ~ ABC