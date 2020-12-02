# Happy Holidays!
# Advent of Code Day 2 - Part 1
# SimZor in Vim on 2020.12.02

with open('puzzle.txt') as read_file:
    lines = [line.rstrip() for line in read_file]
    valid_passwords = 0

    for line in lines:
        separated = line.split()

        requirements = separated[0]
        separated_requirements = requirements.split('-')
        required_character = separated[1][0]
        password = separated[2]

        minimum_occurrences = int(separated_requirements[0])
        maximum_occurrences = int(separated_requirements[1])

        occurrences = password.count(required_character)

        if (
            occurrences >= minimum_occurrences
            and occurrences <= maximum_occurrences
        ):
            valid_passwords = valid_passwords + 1

    print(f'Valid passwords {valid_passwords}')
