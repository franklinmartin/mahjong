## Classes notes

Suit
Tile
Wall

Hand
Player


RiichiMahjongGame




Flow:
Draw Tile.
Check Tsumo, Ron
Check Riichi
Check Kan
Discard

Discard Reaction CHI PON KAN -> RON

LEFTWARD CHI, sequence.
PON (ANY), 
KAN (ANY) -> OPEN, CLOSED, KAN FROM PON


1st: Flow.
Player --- Player ...
Draw Tile, Discard Tile.
Declare win.



MELD: SEQUENCE AND SET
PAIR



Areas to Consider Refining

    Decision Timing & Concurrency:
        Ron Calls: Make sure that the window for declaring Ron (or any reaction call) is clearly defined and that only one valid call can interrupt the game flow. In a real game, these calls are time-sensitive and may occur simultaneously.
        Asynchronous Handling: Especially if integrating AI or a networked UI, consider how asynchronous reactions (multiple players potentially calling Ron) will be managed.

    Furiten Handling:
        Flesh out the furiten logic so that the state is clearly tracked and decisions are made correctly. For example, if a player is in self-furiten, they should be blocked from making certain calls.

    GameState Abstraction:
        Instead of having players reference a full GameState (which in turn references the players), consider using a lightweight snapshot of the state for decision-making. This decoupling can simplify AI integration and avoid potential circular dependencies.

    Edge Cases & Exceptions:
        Identify and document edge cases (e.g., simultaneous Ron declarations or conflicting meld calls) so that the implementation can handle them gracefully.