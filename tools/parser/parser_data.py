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
# Work in Progress Production Rules
# E' -> P
# P -> B
# B -> E B
# B -> { B }
# B -> ''
# E -> E + T
# E -> E - T
# E -> A F = T
# E -> T
# T -> T * F
# T -> T / F
# T -> F ;
# T -> F
# F -> ( E )
# F -> id
# F -> num
# A -> int
# A -> float

# Use this website
#   https://jsmachines.sourceforge.net/machines/slr.html 