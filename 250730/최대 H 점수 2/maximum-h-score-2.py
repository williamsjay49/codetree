import sys
N, L = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
for h in range(100, 0, -1):  # Try H from 100 down to 1
    count_ge_h = 0  # Count of elements ≥ h
    close_enough = []

    for x in a:
        if x >= h:
            count_ge_h += 1
        elif x + 1 >= h:
            close_enough.append(x)  # Candidate for boosting

    # You need at least h elements ≥ h
    needed = h - count_ge_h

    if needed <= len(close_enough) and needed <= L:
        print(h)
        sys.exit()
