import random
from enum import Enum
from typing import List

# Define the tile suits and types.
class Suit(Enum):
    MAN = 'Manzu'
    PIN = 'Pinzu'
    SOU = 'Souzu'
    WIND = 'Wind'
    DRAGON = 'Dragon'

class Tile:
    def __init__(self, suit, value):
        self.suit = suit  # Suit or type of tile
        self.value = value  # Numeric value or name (for winds/dragons)
    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.suit == other.suit and self.value == other.value
    def __repr__(self):
        return f"{self.value} {self.suit.value}"

class Wall:
    def __init__(self):
        self.tiles = self._generate_tiles()
        random.shuffle(self.tiles)

    def _generate_tiles(self):
        tiles = []
        # Create suited tiles (Manzu, Pinzu, Souzu)
        for suit in [Suit.MAN, Suit.PIN, Suit.SOU]:
            for num in range(1, 10):
                tiles.extend([Tile(suit, num) for _ in range(4)])
        # Create honor tiles (Winds)
        for wind in ['East', 'South', 'West', 'North']:
            tiles.extend([Tile(Suit.WIND, wind) for _ in range(4)])
        # Create honor tiles (Dragons)
        for dragon in ['White', 'Green', 'Red']:
            tiles.extend([Tile(Suit.DRAGON, dragon) for _ in range(4)])
        return tiles

    def draw_tile(self):
        """Draws a tile from wall. Returns None if no tiles remain."""
        if self.tiles:
            return self.tiles.pop(0)
        return None

class Hand:
    def __init__(self, open_melds=None):
        self.tiles = []
        self.open_melds = open_melds or []

    def add_tile(self, tile):
        self.tiles.append(tile)

    def remove_tile(self, tile):
        self.tiles.remove(tile)

    def __lt__(self, other: 'Tile'):
        suit_order = {Suit.MAN: 1, Suit.PIN: 2, Suit.SOU: 3, Suit.WIND: 4, Suit.DRAGON: 5}
        if suit_order[self.suit] == suit_order[other.suit]:
            return self.value < other.value
        return suit_order[self.suit] < suit_order[other.suit]

    def is_closed(self):
        return len(self.open_melds) == 0
    
    def is_tenpai(self):
        return False
    
    def __repr__(self):
        return f"Hand({self.tiles})"
    

class Player:
    def __init__(self, name, is_ai=False):
        self.name = name
        self.hand = Hand()
        self.discards = []
        self.score = 25000  # Starting score for each player
        self.is_ai = is_ai

    def draw(self, wall):
        tile = wall.draw_tile()
        if tile:
            self.hand.add_tile(tile)
        return tile

    def discard(self, tile):
        self.hand.remove_tile(tile)
        self.discards.append(tile)
        return tile

    # Placeholder for declaring Riichi. In a full implementation,
    # you would check that the hand is closed and in tenpai.
    def declare_riichi(self):
        print(f"{self.name} declares Riichi!")
        # Deduct 1000 points from score and mark hand as riichi.
        self.score -= 1000
        self.declared_riichi = True
    
    def declare_tsumo():
        return True
    
    def __repr__(self):
        return f"Player({self.name}, Score: {self.score})"
    
class GameState:
    def __init__(self, players, wall, dealer_index=0, round_wind='East'):
        self.players = players
        self.wall = wall
        self.dealer_index = dealer_index
        self.round_wind = round_wind
        self.riichi_declared = False

    def get_game_state(self):
        return {
            "players": self.players,
            "dealer_index": self.dealer_index,
            "round_wind": self.round_wind,
            "wall_tiles_left": len(self.wall.tiles)
        }

class RiichiMahjongGame:
    def __init__(self, players):
        self.players = players
        self.wall = Wall()
        self.dealer_index = 0  # Index for the dealer (East seat)
        self.round_wind = 'East'  # Can change as rounds progress

        self.riichi_declared = False

    def initial_deal(self):
        # Each player receives 13 tiles; dealer gets 14.
        for _ in range(13):
            for player in self.players:
                player.draw(self.wall)
        self.players[self.dealer_index].draw(self.wall)

    def play_turn(self, player):
        drawn_tile = player.draw(self.wall)
        print(f"{player.name} draws {drawn_tile}")
        # Here you would check for a winning condition (Tsumo) or Riichi declaration.
        # For demonstration, we simply discard the first tile in hand.
        if player.hand.tiles:
            tile_to_discard = player.hand.tiles[0]
            discarded_tile = player.discard(tile_to_discard)
            print(f"{player.name} discards {discarded_tile}")

    def play_round(self):
        self.initial_deal()
        turn = self.dealer_index
        # Basic turn loop until the wall is exhausted.
        while self.wall.tiles:
            current_player = self.players[turn % len(self.players)]
            self.play_turn(current_player)
            turn += 1

    #def player_turn(self, player, game_state: GameState):

    def ai_turn(self, player, game_state: GameState):
        if player.is_ai:
            decision = self.ai_decision(game_state)
    def ai_decision(self, game_state: GameState):
        return random.choice(['draw', 'discard', 'declare riichi'])