from .scan_lines import *
from .change_state import *
from .get_token import *
from .dfa import *
from .tokenizer import *
import os

def lexer(filename):
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        print("Please make sure to properly pass the name of the file.")
        print('EXAMPLE: main("case1.in")')
        return

    token_stream = []
    chars_scanned = ""

    # Current state can be derived by rows (meaning state) and columns (meaning input), q0 = row 0
    current_row = 0
    current_column = 0
    token = ""
    comment_detected = False

    input_lines = scan_lines(filename)

    while (True):
        # Go line by line
        for line in input_lines:
            comment_detected = False

            for char in line:
                comment_detected = False
                # Now we are reading each character in each line one by one
                if ((char == "\n") and (len(chars_scanned) == 1)):
                    reject = True

                
                reject = False
                # call function to change state according to input
                list1 = change_state(char, current_row, current_column)

                reject = list1[0]
                current_row = list1[1]
                current_column = list1[2]

                if (reject):
                    # First, get back the appropriate token for chars_scanned
                    if ((chars_scanned == " ") or (chars_scanned == "")):
                        continue
                    token = get_token(current_row)
                    is_keyword = get_keyword(chars_scanned)
                    if is_keyword != "IDENTIFIER":
                        token = is_keyword
                    # token_stream = token_stream + " " + token
                    token_stream.append((token, chars_scanned))
                    # DEBUG: print(f"For '{chars_scanned}', saved '{token}' to token_stream")

                    if (token == "comment"):
                        token = ""
                        chars_scanned = ""
                        current_row = 0
                        comment_detected = True
                        # Skip this line
                        break
                    token = ""
                    chars_scanned = ""
                    current_row = 0
                    list1 = change_state(char, current_row, current_column)

                    reject = list1[0]
                    current_row = list1[1]
                    current_column = list1[2]
                chars_scanned += char
                chars_scanned = chars_scanned.strip()

            if (comment_detected):
                continue
        
        break

    # After finishing scanning all characters, check if there's an unsaved token
    if chars_scanned:
        token = get_token(int(current_row))

        is_keyword = get_keyword(chars_scanned)
        if is_keyword != "IDENTIFIER":
            token = is_keyword
        # token_stream = token_stream + " " + token
        token_stream.append((token, chars_scanned))
        # DEBUG: print(f"For '{chars_scanned}', saved '{token}' to token_stream")

    # print("Token stream:", token_stream)

    # final_token_stream = token_stream.split()
    # print(final_token_stream)

    # return final_token_stream
    return token_stream 

