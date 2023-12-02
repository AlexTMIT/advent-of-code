import re

sum = 0
file = '/Users/atm/Desktop/Personal/AdventOfCode/Puzzle1/inputfile.txt'
pattern = re.compile(r'neight|ne|ight|ine|wo|hree|twone|threeight|fiveight|sevenine|eightwo|eighthree|nineight|one|two|three|four|five|six|seven|eight|nine|\d', re.IGNORECASE)

number_mapping = {
    "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

normal_matches = {
    "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "9": 8, "9": 9
}

check_first = {
    "twone": 2, "threeight": 3, "fiveight": 5, "sevenine": 7,
    "eightwo": 8, "eighthree": 8, "nineight": 9, "neight": 8
}

check_last = {
    "ne": 1, "ight": 8, "ine": 9, "wo": 2, "hree": 3, 
    "twone": 1, "threeight": 8, "fiveight": 8, "sevenine": 9, 
    "eightwo": 2, "eighthree": 3, "nineight": 8, "neight": 8
}

with open(file, 'r') as file: 
    for line in file:
        match = pattern.findall(line)

        print(match)

        if len(match) >= 1:
            # first number should only match 'normal' matches
            if match[0].lower() in normal_matches:
                first_digit = normal_matches.get(match[0])
            elif match[0].lower() in check_first.keys():
                first_digit = check_first.get(match[0])
            else:
                first_digit = match[0].lower()
                first_digit = number_mapping.get(first_digit, first_digit)  # get number or keep last digit

            if match[-1].lower() in check_last.keys():
                second_digit = check_last.get(match[-1])
            else:
                second_digit = match[-1].lower()
                second_digit = number_mapping.get(second_digit, second_digit)

            sum += int(str(first_digit) + str(second_digit))
print(sum)