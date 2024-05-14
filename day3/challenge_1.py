"""The engine schematic (your puzzle input) consists of a visual representation of the engine.
There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number"
and should be included in your sum. (Periods (.) do not count as a symbol.)"""

"""Plan:
Functions should take a line as an input, we will want to have functions
1. is_symbol
2. find all adjacent - returns a tuple containing all
3.get_and_parse_it
4. """


def get_data() -> list[list]:
    with open('input.txt', 'r') as f:
        txt_file = f.readlines()
    data = [line.strip() for line in txt_file]
    return [list(line) for line in data]


def is_symbol(char: str) -> bool:
    """Returns True if the character is a symbol.
       A character is a symbol if it is not a letter and is not a fullstop."""
    return not char.isalpha() and char != '.'


def get_all_adjacent(line: list) -> tuple:
    """Returns a tuple containing all of the adjacent characters."""
    pass


if __name__ == '__main__':
    data = get_data()

    print(get_data())
