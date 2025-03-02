import itertools
from collections import Counter
from enum import Enum

from mahjong import Suit, Tile

def generate_valid_sequences(suit: Suit):
    valid_sequences = []
    
    # Loop through all possible starting values for a sequence
    for i in range(1, 8):  # Values from 1 to 7 (because 1, 2, 3, ..., 7 is the last valid start for a sequence)
        sequence = (i, i+1, i+2)  # Generate the 3-number sequence (i, i+1, i+2)
        
        # Create the Tile objects for each number in the sequence
        valid_sequences.append(tuple(Tile(suit, num) for num in sequence))
    
    return valid_sequences

if __name__ == "__main__":
    test = (Tile(Suit.MAN, 1), Tile(Suit.MAN, 2), Tile(Suit.MAN, 3))
    values = generate_valid_sequences(Suit.MAN)
    print(test)
    print(values)
    print(test in generate_valid_sequences(Suit.MAN))