# X = int(input())

# Please write your code here.

X = int(input())

speed = 1
time = 0
distance = 0

while distance < X:
    next_speed_distance = (speed + 1) * (speed + 2) // 2
    current_speed_distance = speed * (speed + 1) // 2

    distance += speed
    time += 1

    if distance + next_speed_distance <= X:
        speed += 1
    elif distance + current_speed_distance <= X:
        pass  # keep same speed
    else:
        speed -= 1

print(time)
