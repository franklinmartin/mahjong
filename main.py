from mahjong import Player, RiichiMahjongGame
from board import RiichiMahjongBoard
if __name__ == "__main__":
    players = [Player("Alice"), Player("Bob"), Player("Charlie"), Player("Dana")]
    game = RiichiMahjongGame(players)
    board = RiichiMahjongBoard(game)
    board.game.play_turn(Player("Alice"))