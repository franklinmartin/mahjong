yaku_list = [
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
        "name": "Ryanpeikou",
        "han": 3,
        "conditions": {
            "hand_closed": True,
            "identical_sequences": 2
        },
        "notes": "Hand contains two sets of identical sequences (a stronger form of Iipeikou)."
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
        "name": "Chiitoitsu",
        "han": 2,
        "conditions": {
            "seven_pairs": True
        },
        "notes": "Hand consists of exactly seven different pairs."
    },
    {
        "name": "Suu Ankou",
        "han": "Yakuman",
        "conditions": {
            "concealed_triplets": 4
        },
        "notes": "Hand contains four fully concealed triplets."
    },
    {
        "name": "Suu Ankou Tanki",
        "han": "Double Yakuman",
        "conditions": {
            "concealed_triplets": 4,
            "single_wait": True
        },
        "notes": "Winning on a single wait with four concealed triplets."
    },
    {
        "name": "Tsuuiisou",
        "han": "Yakuman",
        "conditions": {
            "all_honor_tiles": True
        },
        "notes": "Hand consists entirely of honor tiles (winds and dragons)."
    }
]

if __name__ == "__main__":
    for yaku in yaku_list:
        print(f"{yaku['name']}: {yaku['notes']}")
