from .change_state import *

def get_token(current_row):
    if current_row == 1:
        return "identifier"
    elif current_row == 2:
        return "minus"
    elif current_row == 3:
        return "decrement"
    elif current_row == 4:
        return "integer"
    elif current_row == 5:
        return "logicNot"
    elif current_row == 6:
        return "notEqual"
    elif current_row == 7:
        return "plus"
    elif current_row == 8:
        return "increment"
    elif current_row == 9:
        return "assignment"
    elif current_row == 10:
        return "equalityComp"
    elif current_row == 11:
        return "lessThan"
    elif current_row == 12:
        return "lessThanEq"
    elif current_row == 13:
        return "greaterThan"
    elif current_row == 14:
        return "greaterThanEq"
    elif current_row == 15:
        return "bitAnd"
    elif current_row == 16:
        return "logicAnd"
    elif current_row == 17:
        return "bitOr"
    elif current_row == 18:
        return "logicOr"
    elif current_row == 19:
        return "leftParen"
    elif current_row == 20:
        return "rightParen"
    elif current_row == 21:
        return "leftBrace"
    elif current_row == 22:
        return "rightBrace"
    elif current_row == 23:
        return "multiply"
    elif current_row == 24:
        return "division"
    elif current_row == 25:
        return "comment"
    elif current_row == 26:
        return "semicolon"
    elif current_row == 27:
        return "dot"
    elif current_row == 28:
        return "leftBracket"
    elif current_row == 29:
        return "rightBracket"
    elif current_row == 30:
        return "comma"
    elif current_row == 31:
        return "modulus"
    else:
        return "error"
