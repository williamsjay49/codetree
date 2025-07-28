import sys
# n 입력
n = int(input())
# hills 입력
hills = [
    int(input())
    for _ in range(n)
]

min_cost = sys.maxsize
for i in range(1, 101):
    cost = 0
    for elem in hills:
        if i <= elem and elem <= i + 17:
            continue
        
        elif i > elem:
            cost += (i - elem) * (i - elem)
        
        else:
            cost += (elem - (i + 17)) * (elem - (i + 17))

    
    min_cost = min(min_cost, cost)

print(min_cost)