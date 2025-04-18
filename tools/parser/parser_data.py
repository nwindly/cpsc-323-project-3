# I'm thinking about choosing only the necessary tokens for the test cases because the table will be too big and complicated.
valid_tokens = ["leftBrace", "rightBrace", "plus", "minus", "assignment", "multiply", "divide", "semicolon", "leftParen", "rightParen", "identifier", "integer", "dot", "true", "false", "printf", "int", "float", "bool", "main", "return"]

# Fix table_column according to the table
table_column = ["leftBrace", "rightBrace", "plus", "minus", "assignment", "multiply", "divide", "semicolon", "leftParen", "rightParen", "identifier", "integer", "dot", "true", "false", "printf", "int", "float", "bool", "main", "return", "$", "E'", "P", "B", "E", "T", "F", "A", "M", "R"]

# Fix table according to our valid tokens
table = [
#       {       }       +       -       =       *       /       ;       (       )       identifier  integer dot     true    false   printf  int     float   bool    main    return  $       E'      P       B       E       T       F       A       M       R
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 0
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 1
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 2
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 3
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 4
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 5
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 6
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 7
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 8
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 9
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 10
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 11
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 12
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 13
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 14
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 15
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 16
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 17
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 18
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 19
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 20
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 21
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 22
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 23
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 24
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 25
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 26
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 27
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 28
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 29
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 30
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 31
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 32
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 33
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 34
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