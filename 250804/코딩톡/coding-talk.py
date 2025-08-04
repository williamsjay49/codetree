# n, m, p = map(int, input().split())
# messages = [tuple(input().split()) for _ in range(m)]
# c = [msg[0] for msg in messages]
# u = [int(msg[1]) for msg in messages]

# names = ['a'] * n
# # Please write your code here.
# for i in range(p - 1, m):
#     if i >= (p - 1) and c[i] not in names:
#         names[i] = c[i]
    
#     if i < p - 1 and u[i] == u[p - 1]:
#         print(c[i])
#         names[i] = c[i]

# print(names)
# for i in range(n):
#     target = ord('A') + i
#     not_found = True
#     for j in range(n):
#         if target == ord(names[j]):
#             not_found = False
#             break
    
#     if not_found:
#         print(chr(target), end=" ")

n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

read = [0] * 26  # Tracks how many times each letter was read

p_person = u[p - 1]  # Person number for the p-th message (0-indexed)

# Count messages *before* p where the receiver is the same as p_person
for i in range(p - 1):
    if u[i] == p_person:
        read[ord(c[i]) - ord('A')] += 1

# Count messages from p (inclusive) to end
for i in range(p - 1, m):
    read[ord(c[i]) - ord('A')] += 1

# Print characters not read by p_person
if p_person != 0:
    for i in range(n):
        if read[i] == 0:
            print(chr(ord('A') + i), end=' ')
