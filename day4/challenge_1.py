
"""Goal, given a row which consists of two lists of numbers found how many numbers the lists have in common, say n numbers then the score is then 2**(n-1)
 tally this score over multiple rows."""

"""Data structure, we want a row to contain two lists. so the data structure for a row is tuple(list,list) where the left list is your card and the right d"""


def open_and_parse_data() -> list:
    """This function opens and parses the data."""
    with open('data.txt') as f:
        data = [line.strip() for line in f.readlines()]
    data = [line.split('|') for line in data]
    parsed_data = []
    for row in data:
        card = [digit for digit in row[0].split(' ') if digit.isdigit()]
        winning_numbs = [digit for digit in list(
            [row[1].split(' ')])[0] if digit.isdigit()]
        parsed_data.append((card, winning_numbs))
    return parsed_data


def count_number_of_matches(card: list, winning_numbs: list) -> int:
    """Counts the number of matches between two lists."""
    return len(set(card).intersection(set(winning_numbs)))


if __name__ == '__main__':
    data = open_and_parse_data()
    count = 0
    for row in data:
        matches = count_number_of_matches(row[0], row[1])
        score = 2**(matches-1) if matches != 0 else 0
        count += score
    print(count)
