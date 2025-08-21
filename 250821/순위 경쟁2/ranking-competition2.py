n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))


# (-) B, (+) A 0 - A, B
# Please write your code here.
arr = [0, 0]
cnt = 1

if c[0] == "A":
    arr[0] = s[0]
else:
    arr[1] = s[0]

diff = arr[0] - arr[1]

for i in range(1, n):
    a, b = c[i], s[i]

    if c[i] == "A":
        arr[0] += s[i]
    else:
        arr[1] += s[i]
    
    if arr[0] - arr[1] == 0 and diff != 0:
        cnt += 1
        diff = 0
    
    elif arr[0] - arr[1] < 0 and diff >= 0:
        cnt += 1
        diff = arr[0] - arr[1]
    
    elif arr[0] - arr[1] > 0 and diff <= 0:
        cnt += 1
        diff = arr[0] - arr[1]

print(cnt)