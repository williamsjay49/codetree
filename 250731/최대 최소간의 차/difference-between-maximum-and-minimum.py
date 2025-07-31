
n, k = map(int, input().split())

num_list = list(map(int, input().split()))
ans = 10000
for i in range(1, 10001):

    new_arr = []
    cost = 0
    for j in range(n):
        if i < num_list[j] < i + k:
            new_arr.append(num_list[j])
            continue
        
        if num_list[j] < i:
            cost += abs(i - num_list[j])
        
        elif num_list[j] > i + k:
            cost += abs(num_list[j] - i - k)
    
    ans = min(ans, cost)


print(ans)