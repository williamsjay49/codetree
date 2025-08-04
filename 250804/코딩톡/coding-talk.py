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
c = [msg[0] for msg in messages]  # sender characters
u = [int(msg[1]) for msg in messages]  # unread counts

# Store unread counts by sender letter
lst = [0] * 26  # lst[0] means for 'A', lst[25] for 'Z'
how = [''] * m  # sender of each message

for i in range(m):
    sender = c[i]
    unread_count = u[i]
    lst[ord(sender) - ord('A')] = unread_count
    how[i] = sender

# If unread count of message p is 0, print nothing
target_sender = how[p - 1]
target_unread_count = lst[ord(target_sender) - ord('A')]

if target_unread_count == 0:
    print("")
    exit()

# Track who has read messages (size n, since people are A to ...)
read = [0] * n  # index 0 → A, 1 → B, etc.

# Count same unread value as message[p] BEFORE message[p]
for i in range(p - 1):
    if lst[ord(how[i]) - ord('A')] == target_unread_count:
        read[ord(how[i]) - ord('A')] += 1

# From message[p] onward, mark as read
for i in range(p - 1, m):
    read[ord(how[i]) - ord('A')] += 1

# Output people (A to ...) who did not read any of those
for i in range(n):
    if read[i] == 0:
        print(chr(ord('A') + i), end=' ')
