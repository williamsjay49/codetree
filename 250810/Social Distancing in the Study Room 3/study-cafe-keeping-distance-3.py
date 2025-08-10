N = int(input())
seats = input()

# Please write your code here.
idx = 0
dist = 0
start = 0
for i in range(1, N):

    Found = True
    if int(seats[i]) == 1:
        idx = i
        dist = (idx - start) // 2
        # print(dist, idx)
        for j in range(idx + 1, N):
            if int(seats[j]) == 1 and (j - idx) < dist:
                start = i
                i = idx + 1

                # print(start, i)
                False
                break
        
            idx = j
        if Found:
            print(dist)
            break
