N = int(input())
str = input()
arr = [0] * 91
# Please write your code here.
for i in range(1, N):
    if str[0] == str[i]:
        temp = str[i::]
        break
cnt = 1
for i in range(len(temp)):
    if temp[i] != str[i]:
        break
    
    cnt += 1

print(cnt)