N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
ans__ = 0
for i in range(N):
    ans = [arr[i]]
    for j in range(i + 1, N):
        

        if 0 <= arr[j] - arr[i] <= K:
            ans.append(arr[j])

    ans__ = max(len(ans), ans__)

print(ans__)
