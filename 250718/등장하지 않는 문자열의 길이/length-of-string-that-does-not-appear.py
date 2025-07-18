# N = int(input())
# str = input()
# arr = [0] * 91
# # Please write your code here.
# for i in range(1, N):
#     if str[0] == str[i]:
#         temp = str[i::]
#         break
# cnt = 1
# for i in range(len(temp)):
#     if temp[i] != str[i]:
#         break
    
#     cnt += 1

# print(cnt)


N = int(input())
s = input()

arr = list(s)

# Run from string length 1 to the entire length  
res = float('inf')

for i in range(1, N + 1):  # Set string length
    tmp = []
    check = False

    for j in range(N - i + 1):  # Starting point
        t = ""
        for k in range(j, j + i):  # Run for the length
            t += arr[k]
        
        if t not in tmp:
            tmp.append(t)
        else:
            check = True
    
    if not check:
        res = min(res, len(tmp[0]))

print(res)
