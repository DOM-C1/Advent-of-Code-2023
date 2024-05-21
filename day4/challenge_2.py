
"""Goal, given a row which consists of two lists of numbers found how many numbers the lists have in common, say n numbers then the score is then 2**(n-1)
 tally this score over multiple rows."""

"""Data structure, we want a row to contain two lists. so the data structure for a row is tuple(list,list) where the left list is your card and the right d"""

"""it sums up all of the number below it and times it by the count."""


def open_and_parse_data(file_name: str) -> list:
    """This function opens and parses the data."""
    with open(file_name) as f:
        data = [line.strip() for line in f.readlines()]
    data = [line.split('|') for line in data]
    parsed_data = []
    for row in data:
        card = [digit for digit in row[0].split() if digit.isdigit()]
        winning_numbs = [digit for digit in row[1].split() if digit.isdigit()]
        parsed_data.append((card, winning_numbs))
    return parsed_data


def count_number_of_matches(card: list, winning_numbs: list) -> int:
    """Counts the number of matches between two lists."""
    return len(set(card).intersection(set(winning_numbs)))


def calculate_total_scratchcards(data: list) -> int:
    total_cards = len(data)
    additional_cards = [0] * total_cards

    def process_card(index: int) -> int:
        if index >= len(data):
            return 0
        card, winning_numbs = data[index]
        matches = count_number_of_matches(card, winning_numbs)
        won_cards = matches

        for i in range(index + 1, index + 1 + matches):
            if i < len(data):
                additional_cards[i] += 1
                won_cards += process_card(i)

        return won_cards

    for i in range(total_cards):
        process_card(i)

    return total_cards + sum(additional_cards)


if __name__ == '__main__':
    data = open_and_parse_data('data.txt')
    total_scratchcards = calculate_total_scratchcards(data)
    print(total_scratchcards)
