# I'm thinking about choosing only the necessary tokens for the test cases because the table will be too big and complicated.
valid_tokens = ["leftBrace", "rightBrace", "plus", "minus", "assignment", "multiply", "divide", "semicolon", "leftParen", "rightParen", "identifier", "integer", "dot", "true", "false", "printf", "int", "float", "bool", "main", "return"]

# Fix table_column according to the table
table_column = ["leftBrace", "rightBrace", "plus", "minus", "assignment", "multiply", "divide", "semicolon", "leftParen", "rightParen", "identifier", "integer", "dot", "true", "false", "printf", "int", "float", "bool", "main", "return", "$", "E'", "P", "B", "E", "T", "F", "A", "M", "R"]

# Fix table according to our valid tokens
table = [
#       {       }       +       -       =       *       /       ;       (       )      identifier  integer   dot     true    false   printf  int     float   bool    main   return    $       E'      P       B       E       T       F       A       M       R
        ["S4",  "R5",   None,   None,   None,   None,   None,   None,   "S12",  None,   "S13",      "S14",  None,   "S15",  "S16",  "S17",   "S9",  "S10",  "S11",   None,  "S18",  "R5",   None,   "1",     "2",   "3",    "8",   "6",     "5",   None,   "7"],  # 0
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "Acc",  None,   None,   None,   None,   None,  None,   None,  None,  None],  # 1
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "R1",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 2
        ["S4",  "R5",   "S20",  "S21",  None,   None,   None,   None,   "S12",  None,   "S13",     "S14",   None,   "S15",  "S16",  "S17",  "S9",   "S10",  "S11",   None,  "S18",   "R5",  None,   None,   "19",   "3",   "8",    "6",      "5",  None,  "7"],  # 3
        ["S4",  "R5",   None,   None,   None,   None,   None,   None,   "S12",  None,   "S13",     "S14",   None,   "S15",  "S16",  "S17",  "S9",   "S10",  "S11",   None,  "S18",   "R5",  None,   None,   "22",   "3",   "8",    "6",      "5",  None,  "7"],  # 4
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",      "S14", None,   "S15",  "S16",  "S17",   None,   None,   None,  "S26",   None,   None,   None,   None,   None,   None,   "25",   "24",   None,   "23",  None],  # 5
        ["R16", "R16",   "R16", "R16",  "S27",  "R16",  "R16",  "S28",  "R16",  "R16",  "R16",     "R16",   None,   "R16",  "R16",  "R16", "R16",  "R16",   "R16",  None,   "R16",   "R16", None,   None,   None,   None,   None,   None,   None,  None,  None],  # 6
        ["R11",  "R11", "R11", "R11",   None,   None,   None,   None,   "R11",   "R11", "R11",     "R11",   None,   "R11",   "R11",  "R11",  "R11", "R11",  "R11",  None,   "R11",   "R11", None,   None,   None,   None,   None,   None,   None,  None,  None],  # 7
        ["R12", "R12",  "R12", "R12",   None,   "S29",  "S30",  None,   "R12",  "R12",  "R12",     "R12",   None,   "R12", "R12",  "R12",   "R12",  "R12",  "R12",  None,   "R12",  "R12",  None,   None,   None,   None,   None,   None,   None,  None,  None],  # 8
        [None,  None,   None,   None,   None,   None,   None,   None,   "R24",  None,  "R24",      "R24",   None,   "R24",  "R24", "R24",   None,   None,   None,  "R24",   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 9
        [None,  None,   None,   None,   None,   None,   None,   None,   "R25",  None,  "R25",      "R25",   None,   "R25", "R25",  "R25",   None,   None,   None,  "R25",   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 10
        [None,  None,   None,   None,   None,   None,   None,   None,   "R26",   None,   "R26",    "R26",   None,   "R26", "R26",  "R26",   None,   None,   None,  "R26",   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 11
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,   "S13",    "S14",   None,   "S15", "S16",  "S17",   "S9",   "S10",  "S11",  None,   "S18",   None,   None,   None,   None,   "31",   "8",   "6",   "32",  None,  "7"],  # 12
        ["R18", "R18",  "R18",  "R18",  "R18",  "R18",  "R18",  "R18",  "R18",  "R18",   "R18",    "R18",   None,   "R18",  "R18",  "R18",  "R18",  "R18",  "R18",  None,   "R18",  "R18",  None,   None,   None,   None,   None,   None,   None,  None,  None],  # 13
        ["R19", "R19",  "R19",  "R19",  "R19",  "R19",  "R19",  "R19",  "R19",  "R19",   "R19",    "R19",   "S33",  "R19",  "R19",  "R19",  "R19",  "R19",   "R19",  None, "R19",   "R19",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 14
        ["R21", "R21",  "R21",  "R21",  "R21",  "R21",  "R21",  "R21",  "R21",  "R21",   "R21",    "R21",   None,   "R21",  "R21",  "R21",  "R21",  "R21",  "R21",  None,  "R21",   "R21",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 15
        ["R22", "R22",  "R22",  "R22",  "R22",  "R22",  "R22",  "R22",  "R22",  "R22",   "R22",    "R22",   None,   "R22",  "R22",  "R22",  "R22",  "R22",  "R22",  None,  "R22",   "R22",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 16
        [None,  None,   None,   None,   None,   None,   None,   None,   "S34",   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 17
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",     "S14",   None,   "S15", "S16",   "S17",   "S9",   "S10",  "S11",  None,  "S18",   None,   None,   None,   None,   "35",   "8",   "6",     "32",  None,  "7"],  # 18
        [None,  "R2",   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "R2",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 19
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",      "S14",  None,   "S15",  "S16",  "S17",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "36",   "37",   None,  None, None],  # 20
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",      "S14",  None,   "S15",  "S16",  "S17",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "38",   "37",   None,  None, None],  # 21
        [None,  "S39",   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 22
        ["S4",  "R5",   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",      "S14",   None,   "S15", "S16",  "S17",   "S9",   "S10",  "S11",   None, "S18",  "R5",   None,   None,   "40",   "3",     "8",    "6",     "5",  None,  "7"],  # 23
        ["R16", "R16",  "R16", "R16",   "S41",  "R16",  "R16",  "S28",  "R16",  "R16",  "R16",      "R16",   None,   "R16",  "R16",  "R16",  "R16",  "R16",  "R16",  None,  "R16"   "R16",  None,   None,   None,   None,   None,   None,   None,  None,  None],  # 24
        ["R9",   "R9",  "R9",   "R9",   None,   "S29",  "S30",  None,    "R9",  "R9",  "R9",         "R9",   "R9",    "R9",   "R9",   "R9",   "R9",  "R9",   "R9",   None,  "R9",    "R9",  None,   None,   None,   None,   None,   None,   None,  None,  None],  # 25
        [None,  None,   None,   None,   None,   None,   None,   None,   "S42",   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 26
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",     "S14",   None,   "S15",  "S16",  "S17",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "43",   "37",   None,  None,  None],  # 27
        ["R15", "R15",  "R15",  "R15",  None,   "R15",  "R15",  None,   "R15",  "R15",  "R15",      "R15",   None,  "R15",  "R15",  "R15",   "R15",  "R15", "R15",   None,  "R15",  "R15",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 28
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",  None,   "S13",      "S14",   None,  "S15",  "S16",  "S17",  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "44",   None,  None,  None],  # 29
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",  None,   "S13",      "S14",   None,  "S15",  "S16",  "S17",  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "45",   None,  None,  None],  # 30
        [None,  None   "S20",  "S21",   None,   None,   None,   None,   None,   "S46",   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 31
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,   "S13",     "S14",   None,  "S15",  "S16",  "S17",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "25",   "24",   None,  None,  None],  # 32
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       "S47",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 33
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,   "S13",     "S14",   None,  "S15",  "S16",  "S17",   "S9",  "S10",  "S11",   None,  "S18",   None,   None,   None,   None,   "48",   "8",   "6",   "32",  None,  "7"],  # 34
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 35
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 36
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 37
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 38
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 39
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 40
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 41
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 42
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 43
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 44
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 45
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 46
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 47
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 48
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 49
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 50
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None]   # 51
]

# Production Rules Done. Passing tokens for both test cases
# E' -> P
# P -> B
# B -> E B
# B -> { B }
# B -> A M B
# B -> ''
# E -> E + T
# E -> E - T
# E -> A F = T
# E -> A T
# E -> F = T
# E -> R
# E -> T
# T -> T * F
# T -> T / F
# T -> F ;
# T -> F
# F -> ( E )
# F -> id
# F -> num
# F -> num . num
# F -> true
# F -> false
# F -> printf ( E )
# A -> int
# A -> float
# A -> bool
# M -> main ( )
# R -> return E

# Use this website
#   https://jsmachines.sourceforge.net/machines/slr.html 

# Both tests cases parsing correctly
# Tokens from test case 1:
# int main ( ) { int id = num ; float id = num . num ; bool id = true ; id = id + num ; id = id + id ; return num ; }

# Tokens from test case 2:
# int main ( ) { int id ; float id = num ; id = num + id ; func ( id ) ; return num . num ; }

productions = {
    1: ("E'", ["P"]),
    2: ("P", ["B"]),
    3: ("B", ["E", "B"]),
    4: ("B", ["leftBrace", "B", "rightBrace"]),
    5: ("B", ["A", "M", "B"]),
    6: ("B", [""]),
    7: ("E", ["E", "plus", "T"]),
    8: ("E", ["E", "minus", "T"]),
    9: ("E", ["A", "F", "assignment", "T"]),
    10: ("E", ["A", "T"]),
    11: ("E", ["F", "assignment", "T"]),
    12: ("E", ["R"]),
    13: ("E", ["T"]),
    14: ("T", ["T", "multiply", "F"]),
    15: ("T", ["T", "divide", "F"]),
    16: ("T", ["F", "semicolon"]),
    17: ("T", ["F"]),
    18: ("F", ["leftParen", "E", "rightParen"]),
    19: ("F", ["identifier"]),
    20: ("F", ["integer"]),
    21: ("F", ["integer", ".", "integer"]),
    22: ("F", ["true"]),
    23: ("F", ["false"]),
    24: ("F", ["printf", "leftParen", "E", "rightParen"]),
    25: ("A", ["int"]),
    26: ("A", ["float"]),
    27: ("A", ["bool"]),
    28: ("M", ["main", "leftParen", "rightParen"]),
    29: ("R", ["return", "E"])
}