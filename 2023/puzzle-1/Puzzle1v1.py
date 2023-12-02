import re
sum = 0
file = '/Users/atm/Desktop/Personal/AdventOfCode/Puzzle1/inputfile.txt'

# 'r' means that we open it in read-only mode.
with open(file, 'r') as file: 
    for line in file:
        # substitues everything that isnt a digit with ''.
        only_numbers = re.sub(r'\D', '', line) 

        if len(only_numbers) == 1:
            # combines the same digit with itself to form a two digit number
            sum += int(only_numbers + only_numbers) 
        elif len(only_numbers) > 1:
            add = int(only_numbers[0] + only_numbers[-1])
            sum += add
print(sum)