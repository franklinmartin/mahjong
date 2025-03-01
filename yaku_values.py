import itertools
from collections import Counter
from enum import Enum

from mahjong import Suit, Tile

def generate_valid_sequences(suit : Suit):
    valid_sequences = []
    for combination in itertools.combinations(range(1, 10), 3):  # All 3-number combinations from 1 to 9
        if combination[0] + 1 == combination[1] and combination[1] + 1 == combination[2]:  # Consecutive numbers
            valid_sequences.append(tuple([Tile(suit, num) for num in combination]))
    return valid_sequences

if __name__ == "__main__":
    test = (Tile(Suit.MAN, 1), Tile(Suit.MAN, 2), Tile(Suit.MAN, 3))
    values = generate_valid_sequences(Suit.MAN)
    print(test)
    print(values)
    print(test in generate_valid_sequences(Suit.MAN))