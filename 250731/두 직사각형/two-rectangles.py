x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.

if a2 < x1 or b2 < y1:
    print("nonoverlapping")

else:
    print("overlapping")