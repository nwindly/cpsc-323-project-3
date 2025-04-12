from . import dfa

def change_state(char, current_row, current_column):
    # Determine the column index for the current character
    if char.isdigit():  # 0-9 
        current_column = 1
    elif char == "-":  # -
        current_column = 2
    elif char == "!":  # !
        current_column = 3
    elif char == "=":  # =
        current_column = 4
    elif char == "+":  # +
        current_column = 5
    elif char == "<":  # <
        current_column = 6
    elif char == ">":  # >
        current_column = 7
    elif char == "&":  # &
        current_column = 8
    elif char == "|":  # |
        current_column = 9
    elif char == "(":  # (
        current_column = 10
    elif char == ")":  # )
        current_column = 11
    elif char == "{":  # {
        current_column = 12
    elif char == "}":  # }
        current_column = 13
    elif char == "*":  # *
        current_column = 14
    elif char == "/":  # /
        current_column = 15
    elif char == ";":  # ;
        current_column = 16
    elif char == ".":  # .
        current_column = 17
    elif char == "[":  # [
        current_column = 18
    elif char == "]":  # ]
        current_column = 19
    elif char == ",":  # ,
        current_column = 20
    elif char == "%":  # %
        current_column = 21
    elif char.isalpha():  # a-Z 
        current_column = 0
    else:
        # If an invalid character is encountered, return immediately
        current_row = int(current_row)
        current_column = int(current_column)
        return [True, current_row, current_column]
    
    # Get the next state from the DFA table using the current row and column
    current_row = int(current_row)
    current_column = int(current_column)
    next_state = dfa.dfa_table[current_row][current_column]

    if next_state is None:
        # If the transition is invalid (None), reject the token
        return [True, current_row, current_column]

    return [False, next_state, current_column]