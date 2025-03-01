from mahjong import Player, RiichiMahjongGame
from board import RiichiMahjongBoard

import random

if __name__ == "__main__":
    players = [Player("Alice"), Player("Bob"), Player("Charlie"), Player("Dana")]
    random.shuffle(players)
    game = RiichiMahjongGame(players)
    board = RiichiMahjongBoard(game)
    board.game.play_round()
    #print(board.game.players[0].hand)
    #print(players[0].hand)