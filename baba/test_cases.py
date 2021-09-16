__all__ = ["TEST_CASES"]

t = {}
t["fastest loss"] = {"sequence": ">>^>>V", "outcome": True}
t["fastest_win"] = {"sequence": "<^<V", "outcome": False}
t["rock_is_baba"] = {"sequence": "<^^^<<V>V<>>", "outcome": True}
t["baba_is_win"] = {"sequence": "<VV<V<<^V>>^<", "outcome": True}
t["rock_is_you"] = {"sequence": "<^^^<<V^<<VV>><<^>><<", "outcome": True}
t["rock_is_win"] = {"sequence": "<VVV<^<^>V>^^V<<<<^^^>^>>>>VVV<^>>>", "outcome": True}
t["rock_is_win_and_push"] = {
    "sequence": "<^<<<<V>>>V>VV<<^^^>^<VV>>V<V<^^>^<V>>>>>>>V<^^^^>^<<<<<<<<<",
    "outcome": True,
}
t["loose_as_flag"] = {"sequence": "<V<<<<V>>V>^^>>^^>>^>>V", "outcome": False}
t["iss_dont_chain_through_properties"] = {
    "sequence": "<V<<<<V>>V>>^^VV>^^",
    "outcome": False,
}
t["iss_chain_through_nouns"] = {
    "sequence": "<V<<V^<V>>>^^<^>^^<<V^<<VV>>>^>VVVV^^^<<<<^>>^>VVVV>>V^<<V>>^^>>",
    "outcome": True,
}
t["flag_is_rock_is_win"] = {
    "sequence": ">VV>^^<^>V>^VV<<<<<<<V^>V>>^>V^^<<^>^^<<V^<<VV>>>^>VVVV^^^<<<<^>>^>VVVVV^^>>>>>>",
    "outcome": True,
}
t["rules_dont_work_upside_down"] = {
    "sequence": "<V<<<<V>>V>>>^V<<<^>V>>^V<<^>V>>^^^>>^>>V",
    "outcome": False,
}
t["rules_dont_work_right_to_left"] = {
    "sequence": "<V<<<<V>>V>>>^V<<<^>V>>^V<<^>><^^^>V>V<^<V<VV>>>>^<<<>^^>>^>>V",
    "outcome": False,
}
t["rules_act_alphabetically_1"] = {
    "sequence": "<^<<<<V>>^<<^^>>V^<<VV>>^><V><V><<<VVV>^^<^>>V>^^<^>VVV>VV<<^^^<^>V>^<^>><<V<<^>>>>>V<^<VV<<",
    "outcome": True,
}
t["rules_act_alphabetically_2"] = {
    "sequence": "<^<<<<V>>^<<^^>>VV<V>V>>VV<<^V<<^>^^^<^>^>VV>V<V<V>^^>V>V>>>^^<<",
    "outcome": True,
}
t["everything_is_flag"] = {
    "sequence": "<^^^<<V^<<V><VVVVV>>^V<<^>^<^><",
    "outcome": False,
}
t["walk_into_a_corner"] = {
    "sequence": (
        "VVVV>>>>>>>>^^^^^^^>^^>^^^>>>^>^>^>^>^>^>^^>^<<<<<<<<<<<<<VVVVVVV^^>>>>>>>>^>"
    ),
    "outcome": True,
}
t["rock_is_baba_is_win"] = {
    "sequence": ">>V>V<<<V<<<^V<<^><^^^^^>>V^<<V><VV><",
    "outcome": True,
}

TEST_CASES = t

if __name__ == "__main__":
    import os, json

    filename = os.path.realpath("./test_data.json")
    with open(filename, "w") as f:
        json.dump(t, f, indent="  ")
