steps = 0

with open('sample-input.txt', 'r') as file:
    lines = file.readlines()

instructions = list(lines[0].strip())
dictionary = {}

for line in lines[1:]:
    if "=" in line:
        key, values = line.strip().split("=")
        values = values.replace("(", "").replace(")", "").split(", ")
        dictionary[key.strip()] = values

print(instructions)
print(dictionary)

