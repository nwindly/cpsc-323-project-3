token_names = ["integer", "identifier", "number", "comment", "leftParen", "rightParen", "leftBracket", "rightBracket", "leftBrace", "rightBrace", "dot", "plus", "minus", "multiply", "divide", "modulus", "lessThan", "greaterThan", "assignment", "semicolon", "comma", "increment", "decrement", "lessThanE", "greaterThanE", "logicEual", "logicANd", "logicOr", "logicNot", "bitAnd", "bitOr"]

# true or false will be considered as an identifier for the parser because the job is for semantic
token_keywords = ["bool", "int", "return", "if", "switch", "float", "while", "else", "case", "char", "for", "goto", "unsigned", "main", "break", "continue", "void"]

dfa_table = [ 
#  a-Z    0-9   -     !     =     +     <      >     &    |     (      )    {     }      *     /    ;    .        [    ]      ,    %
  ["1",  "4",  "2",  "5",  "9",  "7",  "11", "13", "15", "17", "19", "20", "21", "22", "23", "24", "26", "27", "28", "29", "30", "31"],  # 0
  ["1",  "1",  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 1 Identifier/Variable
  [None, "4",  "3",  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 2 Minus
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 3 Decrement Operator
  [None, "4",  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 4 Numbers/Integer
  [None, None, None, None, "6", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 5 Logical Not Operator
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 6 Not Equal Operator
  [None, None, None, None, None, "8", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 7 Plus
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 8 Increment Operator
  [None, None, None, None, "10", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 9 Assignment Operator
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 10 Equality Comparison Operator
  [None, None, None, None, "12", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 11 Less than
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 12 Less than, Equal to
  [None, None, None, None, "14", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 13 Greater than
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 14 Greater than, Equal to
  [None, None, None, None, None, None, None, None, "16", None, None, None, None, None, None, None, None, None, None, None, None, None],  # 15 Bit And
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 16 Logic And
  [None, None, None, None, None, None, None, None, None, "18", None, None, None, None, None, None, None, None, None, None, None, None],  # 17 Bit Or
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 18 Logic Or
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 19 Left Parenthesis
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 20 Right Parenthesis
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 21 Left Curly Brace
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 22 Right Curly Brace
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 23 Multiplication Operator
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "25", None, None, None, None, None, None],  # 24 Division
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 25 Comment
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 26 Semicolon
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 27 Dot
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 28 Left Bracket
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 29 Right Bracket
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 30 Comma
  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # 31 Modulus
]
