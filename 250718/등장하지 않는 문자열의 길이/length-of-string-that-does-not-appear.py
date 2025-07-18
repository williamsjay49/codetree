N = int(input())
str = input()

ans = 1
for i in range(1, N):
    twice = False

    for j in range(N - i + 1):
        for k in range(j + 1, N - i + 1):

            issame = True
            for l in range(i):
                if str[j + l] != str[k + l]:
                    issame = False

            if issame:
                twice = True    

    if twice:
        ans += 1

print(ans)