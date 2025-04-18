# Plan:
# I'm thinking about choosing only the necessary tokens for the test cases because the table will be too big and complicated.

valid_tokens = ["int", "main", "leftParen", "rightParen", "leftBrace", "rightBrace", "identifier", "assignment", "integer", "semicolon", "float", "dot", "bool", "plus", "return"]

# TO DO: fix table_column according to the table
table_column = []

# TO DO: fix table according to our valid tokens
table = [
#     id     +     -      *     /    (      )     $     E      T      F  
    ["S5",  None, None, None, None, "S4", None, None,  "1",   "2",   "3"  ],  # state 0
    [None,  "S6", "S7", None, None, None, None, "Acc", None, None, None ],  # state 1
    [None,  "R3", "R3", "S8", "S9", None, "R3", "R3",  None, None, None ],  # state 2
    [None,  "R6", "R6", "R6", "R6", None, "R6", "R6",  None, None, None ],  # state 3
    ["S5",  None, None, None, None, "S4", None, None, "10",  "2",   "3"  ],  # state 4
    [None,  "R8", "R8", "R8", "R8", None, "R8", "R8",  None, None, None ],  # state 5
    ["S5",  None, None, None, None, "S4", None, None, None,  "11",  "3"  ],  # state 6
    ["S5",  None, None, None, None, "S4", None, None, None,  "12",  "3"  ],  # state 7
    ["S5",  None, None, None, None, "S4", None, None, None,  None,  "13" ],  # state 8
    ["S5",  None, None, None, None, "S4", None, None, None,  None,  "14" ],  # state 9
    [None,  "S6", "S7", None, None, None, "S15", None, None, None, None ],  # state 10
    [None,  "R1", "R1", "S8", "S9", None, "R1", "R1",  None, None, None ],  # state 11
    [None,  "R2", "R2", "S8", "S9", None, "R2", "R2",  None, None, None ],  # state 12
    [None,  "R4", "R4", "R4", "R4", None, "R4", "R4",  None, None, None ],  # state 13
    [None,  "R5", "R5", "R5", "R5", None, "R5", "R5",  None, None, None ],  # state 14
    [None,  "R7", "R7", "R7", "R7", None, "R7", "R7",  None, None, None ]   # state 15
]

# TO DO: fix productions accordingly
productions = {
    1: ("P", ["F"]),
    2: ("F", ["T", "main", "leftParen", "rightParen", "B"]),
    3: ("T", ["int"]),
    4: ("T", ["float"]),
    5: ("T", ["bool"]),
    6: ("B", ["leftBrace", "S", "rightBrace"]),
    7: ("S", ["S", "S"]),
    8: ("S", ["S"]),
    9: ("S", ["D"]),
    10: ("S", ["A"]),
    11: ("S", ["R"]),
    12: ("D", ["Type", "id", "assignment", "V", "semicolon"]),
    13: ("A", ["id", "assignment", "E", "semicolon"]),
    14: ("R", ["return", "V", "semicolon"]),
    15: ("E", ["id"]),
    16: ("E", ["V"]),
    17: ("E", ["E", "plus", "E"]),
    18: ("V", ["integer"]),
    19: ("V", ["integer", "dot", "integer"]),
    20: ("V", ["id"]),
    21: ("V", ["true"])
}
