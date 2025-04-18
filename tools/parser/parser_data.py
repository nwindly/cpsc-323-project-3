# I'm thinking about choosing only the necessary tokens for the test cases because the table will be too big and complicated.
valid_tokens = ["int", "main", "leftParen", "rightParen", "leftBrace", "rightBrace", "identifier", "assignment", "integer", "semicolon", "float", "dot", "bool", "plus", "return"]

# Fix table_column according to the table
table_column = ["int", "main", "leftParen", "rightParen", "leftBrace", "rightBrace", "identifier", "assignment", "integer", "semicolon", "float", "dot", "bool", "plus", "return", "$", "P", "F", "T", "B", "S", "A", "R", "D", "V", "E"]

# Fix table according to our valid tokens
table = [
#       int     main    leftParen rightParen leftBrace rightBrace identifier assignment integer semicolon float   dot    bool   plus   return  $     P     F     T     B     S     A     R     D     V     E
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 0
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 1
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 2
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 3
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 4
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 5
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 6
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 7
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 8
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 9
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 10
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 11
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 12
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 13
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 14
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None],  # 15
        [None,  None,   None,     None,      None,     None,      None,      None,      None,   None,     None,  None,  None,  None,  None,   None, None, None, None, None, None, None, None, None, None, None]   # 16
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
