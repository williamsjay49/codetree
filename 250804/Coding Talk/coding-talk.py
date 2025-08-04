n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

names = ['a'] * n
# Please write your code here.
for i in range(m):
    if i >= (p - 1) and c[i] not in names:
        names[i] = c[i]
    
    if i < p - 1 and u[i] == u[p - 1]:
        names[i] = c[i]

# print(names)
for i in range(n):
    target = ord('A') + i
    not_found = True
    for j in range(n):
        if target == ord(names[j]):
            not_found = False
            break
    
    if not_found:
        print(chr(target), end=" ")

