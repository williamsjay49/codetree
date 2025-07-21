n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def satisfy(x):
    for a, b in ranges:
        x *= 2
        if x < a or x> b:
            return False
    
    return True
    



for i in range(1, 100001):

    if satisfy(i):
        print(i)
        break
