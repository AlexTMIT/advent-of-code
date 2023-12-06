import re

total = 1

with open('input.txt', 'r') as file:
    times = file.readline().strip().split()
    distances = file.readline().strip().split()

for i in range (1, 5):
    add = 0
    time = int(times[i])
    record_distance = int(distances[i])

    for j in range (0, time):
        distance = (time - j) * j

        if distance > record_distance:
            add += 1
    
    total *= add

print(total)