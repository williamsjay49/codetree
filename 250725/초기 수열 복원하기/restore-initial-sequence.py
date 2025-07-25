n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.
ranges = []
idx = 1
arr = [0] * n
for p, el in enumerate(adjacent):
    
    for i in range(1, n + 1):
        find = False

        for j in range(1, n + 1):
            # print(abs(el - i), abs(el - j))
            if abs(el - i) == j and abs(el - j) == i and (i, j) not in ranges:
                ranges.append((i, j))
                find = True
                break

        if find:
            break

def overlap(m):
    cnt = [ranges[m][0], ranges[m][1], ranges[m+1][0], ranges[m+1][1]]

    for i in range(1, n + 1):
        if cnt.count(i) == 2:
            return i
    
        
    

for i in range(n - 2):
    # print(overlap(i))
    arr[idx] = overlap(i)
    idx += 1

a, b = ranges[0]
c, d = ranges[-1]

if a == arr[1]:
    arr[0] = b

else:
    arr[1] = a

if c == arr[n - 2]:
    arr[n - 1] = d

else:
    arr[n - 1] = c

for el in arr:
    print(el, end=" ")

# print(arr)
               