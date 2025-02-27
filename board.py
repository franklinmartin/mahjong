from mahjong import RiichiMahjongGame
class RiichiMahjongBoard:
    def __init__(self, game : RiichiMahjongGame):
        self.game = game
        print(game.players)
