# riichi_yaku.py

yaku_list = [
    # Basic Yaku (1-Han)
    {
        "name": "Riichi",
        "han": 1,
        "conditions": {
            "hand_closed": True,
            "tenpai": True,
            "declared": True
        },
        "notes": "Player must be in tenpai with a closed hand and explicitly declare Riichi."
    },
    {
        "name": "Double Riichi",
        "han": 2,
        "conditions": {
            "hand_closed": True,
            "tenpai": True,
            "declared_on_first_turn": True
        },
        "notes": "Declared on the initial dealt hand (immediately after the deal) while in tenpai."
    },
    {
        "name": "Ippatsu",
        "han": 1,
        "conditions": {
            "riichi_recent": True,
            "within_one_turn": True,
            "no_calls": True
        },
        "notes": "Win within one turn after declaring Riichi, before any opponent calls interrupt play."
    },
    {
        "name": "Menzen Tsumo",
        "han": 1,
        "conditions": {
            "hand_closed": True,
            "win_by_tsumo": True
        },
        "notes": "A self-drawn win using a completely closed hand."
    },
    {
        "name": "Pinfu",
        "han": 1,
        "conditions": {
            "hand_closed": True,
            "all_sequences": True,
            "pair_non_value": True,
            "two_sided_wait": True
        },
        "notes": "Hand is made entirely of sequences, with a non-scoring pair and a two-sided wait."
    },
    {
        "name": "Tanyao",
        "han": 1,
        "conditions": {
            "no_terminals": True,
            "no_honors": True
        },
        "notes": "All tiles in the hand are simples (numbers 2–8) with no terminals or honors."
    },
    {
        "name": "Iipeikou",
        "han": 1,
        "conditions": {
            "hand_closed": True,
            "identical_sequences": 1
        },
        "notes": "Hand contains one set of identical sequences."
    },
    {
        "name": "Yakuhai (Seat Wind)",
        "han": 1,
        "conditions": {
            "pair": True,
            "tile_type": "wind",
            "matches_seat": True
        },
        "notes": "A pair of wind tiles matching the player's seat wind."
    },
    {
        "name": "Yakuhai (Prevalent Wind)",
        "han": 1,
        "conditions": {
            "pair": True,
            "tile_type": "wind",
            "matches_round": True
        },
        "notes": "A pair of wind tiles that match the prevailing (round) wind."
    },
    {
        "name": "Yakuhai (Dragons)",
        "han": 1,
        "conditions": {
            "pair": True,
            "tile_type": "dragon"
        },
        "notes": "A pair of any dragon tile (White, Green, or Red)."
    },
    
    # 2-Han Yaku
    {
        "name": "San Shoku Doujun",
        "han": {"closed": 2, "open": 1},
        "conditions": {
            "sequences_in_all_three_suits": True,
            "same_numbers": True
        },
        "notes": "Identical sequences (with the same numerical run) appear in all three suits."
    },
    {
        "name": "Ittsuu",
        "han": {"closed": 2, "open": 1},
        "conditions": {
            "sequence_1_to_9_in_one_suit": True
        },
        "notes": "A complete 1-9 straight exists in one suit."
    },
    {
        "name": "Toitoi",
        "han": 2,
        "conditions": {
            "all_triplets": True
        },
        "notes": "Hand is composed entirely of triplets (and/or quads), with no sequences."
    },
    {
        "name": "San Ankou",
        "han": 2,
        "conditions": {
            "concealed_triplets": 3
        },
        "notes": "Hand contains three triplets that are completely concealed (not melded)."
    },
    {
        "name": "San Shoku Doukou",
        "han": {"closed": 2, "open": 2},
        "conditions": {
            "triplets_in_all_three_suits": True,
            "same_number": True
        },
        "notes": "Triplets or quads of the same number appear in all three suits."
    },
    {
        "name": "Chanta",
        "han": {"closed": 2, "open": 1},
        "conditions": {
            "every_set_contains_terminal_or_honor": True,
            "pair_terminal_or_honor": True
        },
        "notes": "Every meld and the pair must contain at least one terminal or honor tile."
    },
    {
        "name": "Shousangen",
        "han": 2,
        "conditions": {
            "dragon_triplets": 2,
            "dragon_pair": 1
        },
        "notes": "Hand contains two dragon triplets and a pair of the remaining dragon."
    },
    {
        "name": "Honroutou",
        "han": {"closed": 2, "open": 1},
        "conditions": {
            "all_tiles_terminal_or_honor": True
        },
        "notes": "All tiles in the hand are either terminals or honors."
    },
    {
        "name": "Chiitoitsu",
        "han": 2,
        "conditions": {
            "hand_closed": True,
            "seven_pairs": True
        },
        "notes": "Hand is composed of seven distinct pairs."
    },
    
    # Higher Value Yaku (3-6 Han)
    {
        "name": "Ryanpeikou",
        "han": 3,
        "conditions": {
            "hand_closed": True,
            "identical_sequences": 2
        },
        "notes": "Hand contains two sets of identical sequences (a stronger form of Iipeikou)."
    },
    {
        "name": "Junchan",
        "han": {"closed": 3, "open": 2},
        "conditions": {
            "every_set_has_terminal": True,
            "pair_is_terminal": True
        },
        "notes": "Every meld must include a terminal tile and the pair must also be a terminal."
    },
    {
        "name": "Honitsu",
        "han": {"closed": 3, "open": 2},
        "conditions": {
            "main_suit": True,
            "may_include_honors": True
        },
        "notes": "All tiles are from one suit plus honors."
    },
    {
        "name": "Chinitsu",
        "han": {"closed": 6, "open": 5},
        "conditions": {
            "single_suit": True,
            "no_honors": True
        },
        "notes": "All tiles come from one suited type (Manzu, Pinzu, or Souzu) with no honor tiles."
    },
    
    # Yakuman Hands (Special Highest-Ranked Hands)
    {
        "name": "Kokushi Musou",
        "han": "Yakuman",
        "conditions": {
            "contains_each_terminal_and_honor": True,
            "one_duplicate": True
        },
        "notes": "Hand contains one of each of the 13 unique terminal/honor tiles plus an extra duplicate of one."
    },
    {
        "name": "Daisangen",
        "han": "Yakuman",
        "conditions": {
            "dragon_triplets": 3
        },
        "notes": "Hand contains triplets or quads of all three dragon tiles."
    },
    {
        "name": "Shousuushii",
        "han": "Yakuman",
        "conditions": {
            "wind_triplets": 3,
            "wind_pair": 1,
            "at_least_concealed": True
        },
        "notes": "Hand contains triplets (or quads) of three different winds plus a pair of the fourth wind."
    },
    {
        "name": "Daisuushii",
        "han": "Yakuman",
        "conditions": {
            "wind_triplets": 4
        },
        "notes": "Hand contains triplets (or quads) of all four wind tiles."
    },
    {
        "name": "Suu Ankou",
        "han": "Yakuman",
        "conditions": {
            "concealed_triplets": 4
        },
        "notes": "Hand contains four concealed triplets."
    },
    {
        "name": "Suu Ankou Tanki",
        "han": "Double Yakuman",
        "conditions": {
            "concealed_triplets": 4,
            "single_wait": True
        },
        "notes": "Hand with four concealed triplets, where the winning tile completes one of them as a single wait."
    },
    {
        "name": "Tsuuiisou",
        "han": "Yakuman",
        "conditions": {
            "all_honors": True
        },
        "notes": "Hand is composed entirely of honor tiles."
    },
    {
        "name": "Chinroutou",
        "han": "Yakuman",
        "conditions": {
            "all_terminals": True
        },
        "notes": "Hand is composed entirely of terminal tiles (1s and 9s)."
    },
    {
        "name": "Ryuuiisou",
        "han": "Yakuman",
        "conditions": {
            "only_green_tiles": True
        },
        "notes": "Hand is made up entirely of green tiles (2, 3, 4, 6 of Souzu, and Green Dragon)."
    },
    {
        "name": "Chuuren Poutou",
        "han": "Yakuman",
        "conditions": {
            "one_suit": True,
            "nine_gates_pattern": True
        },
        "notes": "Hand in one suit with a specific pattern (1112345678999) that qualifies as Nine Gates."
    },
    {
        "name": "Chuuren Poutou 9-Wait",
        "han": "Double Yakuman",
        "conditions": {
            "one_suit": True,
            "pure_nine_gates": True
        },
        "notes": "Hand qualifies for Pure Nine Gates with a 9-tile wait, considered a Double Yakuman."
    },
    {
        "name": "Tenhou",
        "han": "Yakuman",
        "conditions": {
            "dealer": True,
            "initial_hand_win": True
        },
        "notes": "Dealer wins on the initial dealt hand (instant win)."
    },
    {
        "name": "Chiihou",
        "han": "Yakuman",
        "conditions": {
            "non_dealer": True,
            "initial_hand_win": True
        },
        "notes": "Non-dealer wins on the initial drawn tile (instant win)."
    },
    {
        "name": "Renhou",
        "han": "Yakuman or Mangan",
        "conditions": {
            "special_exception": True
        },
        "notes": "Special case hand; sometimes awarded as Yakuman or Mangan based on regional rules."
    },
    {
        "name": "Dai Sharin",
        "han": "Yakuman (Regional)",
        "conditions": {
            "special_pattern": True
        },
        "notes": "A regional Yakuman hand with a unique tile pattern."
    },
    
    # Special Situational Yaku
    {
        "name": "Rinshan Kaihou",
        "han": 1,
        "conditions": {
            "win_on_replacement_tile_after_kan": True
        },
        "notes": "Win on a tile drawn from the dead wall after a Kan is declared."
    },
    {
        "name": "Chankan",
        "han": 1,
        "conditions": {
            "win_on_discard_during_kan": True
        },
        "notes": "Win by robbing an opponent’s Kan declaration."
    },
    {
        "name": "Haitei Raoyue",
        "han": 1,
        "conditions": {
            "win_on_last_tile": True,
            "tile_drawn": True
        },
        "notes": "Win is declared by drawing the very last tile from the wall."
    },
    {
        "name": "Houtei Raoyui",
        "han": 1,
        "conditions": {
            "win_on_last_discard": True
        },
        "notes": "Win is declared by claiming the last discard of the round."
    },
    {
        "name": "Nagashi Mangan",
        "han": "Mangan",
        "conditions": {
            "only_discards_are_terminals_and_honors": True,
            "none_claimed": True
        },
        "notes": "If a player discards only terminals and honors and none are claimed, they may be awarded Mangan."
    }
]

if __name__ == "__main__":
    # For demonstration, print the list of yaku names and their notes.
    for yaku in yaku_list:
        print(f"{yaku['name']}: {yaku['notes']}")
