n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]

dat = {}
answer = 0
answer_num = 0

for i in range(n):
    for j in range(i - k, i + k + 1):
        if j < 0 or j >= n or i == j:
            continue
        if num[i] == num[j]:
            if num[i] not in dat:
                dat[num[i]] = 0
            dat[num[i]] += 1
            if dat[num[i]] > answer:
                answer = dat[num[i]]
                answer_num = num[i]
            break

print(answer_num)
