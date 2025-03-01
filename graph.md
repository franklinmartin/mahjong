  ```mermaid
  flowchart TD
  %% --- GAME SETUP ---
  A[Game Start] -->|Shuffle Wall and Form Dora Indicator| B[Deal 13 Tiles]
  B -->|Decide First Dealer Oya| C[Game Begins]
  
  %% --- TURN STRUCTURE ---
  C -->|Draw a Tile| D{Action Decision?}

  %% --- PLAYER OPTIONS ---
  D -->|Declare Riichi if Tenpai and Closed| E[Riichi Declared]
  D -->|Declare Kan if Quad Formed| F[Kan Declared]
  D -->|Win with Tsumo| O[Winning Hand Check]
  D -->|Discard Tile| G[Tile Discarded]

  %% --- RIICHI MECHANICS ---
  E -->|Place 1000 Points Bet| H[Riichi Stick Placed]
  H -->|Ippatsu Possible| J[Check Next Discard]
  J -->|Win with Ippatsu| O
  J -->|No Win| C

  %% --- KAN MECHANICS ---
  F -->|Draw Rinshan Tile| K[Rinshan Draw]
  K -->|Win on Rinshan| O
  K -->|No Win| C
  F -->|Draw Additional Dora Indicator| C

  %% --- DISCARD REACTIONS ---
  G -->|Can Opponents Call| L{Call Possible?}
  L -->|Chi for Left Player| M1[Form Chi Meld]
  L -->|Pon for Any Player| M2[Form Pon Meld]
  L -->|Kan for Any Player| M3[Form Open Kan]
  L -->|Ron Win on Discard| O
  L -->|No Call| N[Next Player's Turn]

  %% --- FURITEN CHECK ---
  L -->|Furiten| L1{Self-Furiten?}
  L1 -->|Yes| N
  L1 -->|No| L

  %% --- NEXT TURN HANDLING ---
  M1 --> C
  M2 --> C
  M3 -->|Draw Dora Indicator for Kan| C
  N --> C

  %% --- WINNING HAND CHECK ---
  O[Winning Hand Check] -->|Valid Yaku| P{Has Yaku?}
  P -->|Yes| Q[Scoring and Payment]
  P -->|No Nagashi Mangan Check| R{All Terminals and Honors Discarded?}
  R -->|Yes| Q
  R -->|No| C

  %% --- SPECIAL WINNING CASES ---
  Q -->|Tsumo| Q1[Everyone Pays]
  Q -->|Ron| Q2{Multiple Ron?}
  Q2 -->|Single Ron| S[Final Score Count]
  Q2 -->|Double Ron Ron on same tile| S
  Q2 -->|Triple Ron Paoron Last Ron Blocks Others| S
  Q2 -->|Chankan Robbing a Kan| S
  Q2 -->|Haitei Last Draw Win| S
  Q2 -->|Houtei Last Discard Win| S

  %% --- SCORING and HAND END ---
  S -->|Han and Fu Calculation| T[Final Score Count]
  T -->|Yakuman Check| U{Yakuman or Double Yakuman?}
  U -->|Yakuman| V[Apply Yakuman Payment]
  U -->|Double Yakuman| W[Apply Double Yakuman Payment]
  U -->|Regular Hand| X[Apply Han-Based Payment]

  %% --- DEALER ROTATION ---
  X -->|Dealer Wins| Y{Does Dealer Continue?}
  Y -->|Yes| C
  Y -->|No| Z[Rotate Dealer]

  %% --- END OF GAME CHECK ---
  Z -->|End After Final Round| AA{Game Over?}
  AA -->|Yes| AB[Final Scoring and Winner Declared]
  AA -->|No| C

  %% --- SPECIAL CASES ---
  AB -->|Abortive Draws| AC{9 Terminals Start or 4 Riichi?}
  AC -->|Yes Restart Hand| A
  AC -->|No| AD[Game Ends]
```