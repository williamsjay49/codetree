n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# a, b > interval
# x 

for j in range(1, 10000):

    cnt = 0
    cur = j
    for a, b in ranges:
        exist = False
        while True:
            if a <= cur <= b:
                # print(cur, a, b, cnt)
                cur *= 2
                exist = True
            else:
                break
        
        if exist:
            cnt += 1
    if cnt == n: 
        print(j)

        break