n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_moves = 0
i = j = 0  # pointers

while i < n and j < n:
    # Skip houses that already have desired number of people
    while i < n and A[i] == B[i]:
        i += 1
    while j < n and A[j] == B[j]:
        j += 1
    
    if i == n or j == n:
        break

    # If A[i] > B[i], we have excess people at i
    if A[i] > B[i]:
        # If A[j] < B[j], we need people at j
        if A[j] < B[j]:
            move = min(A[i] - B[i], B[j] - A[j])
            A[i] -= move
            A[j] += move
            total_moves += move * abs(j - i)
        else:
            j += 1
    else:
        i += 1

print(total_moves)
