from cgi import print_arguments
import re
def main():
    points = 0

    with open('puzzle-4/input-file.txt', 'r') as file:
        for line in file:
            winning_numbers = line.split('|')[0].split(': ')[1].strip().split()
            my_numbers = line.split('|')[1].strip().split()
            matches = []

            for number in my_numbers:
                if number in winning_numbers:
                    matches.append(int(number))
                    
            points += get_points(len(matches))
                
    print(points)

def get_points(length):
    if length <= 0:
        return 0
    if length <= 1:
        return 1
    return get_points(length-1) * 2

main()