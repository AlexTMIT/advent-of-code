steps = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()

instructions = list(lines[0].strip())
dictionary = {}

for line in lines[1:]:
    if "=" in line:
        key, values = line.strip().split("=")
        values = [v.strip() for v in values.replace("(", "").replace(")", "").split(",")]
        dictionary[key.strip()] = values

index = -1
key = 'AAA'
travelling = True

while travelling:
    index += 1

    if (key == "ZZZ"):
        travelling = False
        break;
    if (len(instructions) <= index):
        index = 0
    if (instructions[index] == "R"):
        key = dictionary[key][1] 
    else: 
        key = dictionary[key][0] 
    
    steps += 1

print(steps)