# N, K = map(int, input().split())
# arr = [int(input()) for _ in range(N)]

# # Please write your code here.
# ans__ = 0
# for i in range(1, N):
#     cnt = 0
        
#     for el in arr:
#         if i <= el <= K + i:
#             cnt += 1

#     ans__ = max(cnt, ans__)

# print(ans__)


N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Step 1: Create a frequency array to count occurrences of each value in arr
max_value = max(arr)  # We don't need to consider values larger than the largest element in arr
frequency = [0] * (max_value + 1)

# Populate the frequency array
for num in arr:
    frequency[num] += 1

# Step 2: Create a prefix sum array for range queries
prefix_sum = [0] * (max_value + 1)
prefix_sum[0] = frequency[0]

for i in range(1, max_value + 1):
    prefix_sum[i] = prefix_sum[i - 1] + frequency[i]

# Step 3: Calculate the maximum count for any range [i, K + i]
ans = 0
for i in range(1, max_value + 1):
    # Range [i, K + i], make sure K + i does not exceed the max value in the array
    end = min(i + K, max_value)
    count_in_range = prefix_sum[end] - (prefix_sum[i - 1] if i > 1 else 0)
    ans = max(ans, count_in_range)

print(ans)
