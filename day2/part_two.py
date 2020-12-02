# Happy Holidays!
# Advent of Code Day 2 - Part two
# SimZor in Vim on 2020.12.02

with open('puzzle.txt') as read_file:
    lines = [line.rstrip() for line in read_file]
    valid_passwords = 0

    for line in lines:
        separated = line.split()

        requirements = separated[0]
        valid_positions = [int(n) for n in requirements.split('-')]
        required_character = separated[1][0]
        password = separated[2]

        try:
            result = [
                required_character == password[position-1]
                for position
                in valid_positions
            ]

            if (result[0] != result[1]):
                valid_passwords = valid_passwords + 1

        except IndexError:
            pass

    print(f'Valid passwords {valid_passwords}')
