MAX_NUM = 10000

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(1, MAX_NUM + 1):
    possible = True
    section = 1
    total = 0

    for j in range(n):
        if a[j] > i:
            possible = False
            break
        if total + a[j] > i:
            total = 0
            section += 1
        total += a[j]

    if possible and section <= m:
        print(i)
        break
