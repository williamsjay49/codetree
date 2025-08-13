import sys
n = int(input())
arr = list(input().split())

# Please write your code here.
matched = [chr(ord("A") + i) for i in range(n)]
cnt = 0

def rearrange():
    global cnt
    for i in range(1, n):

        for j in range(i + 1, n):
            if ord(arr[i]) > ord(arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
                cnt += 1
                # print(arr)
            break

if arr == matched:
    print(0)
    sys.exit()
Found = True
while Found:
    rearrange()
    if arr == matched:
        Found = False
        break
print(cnt)
        