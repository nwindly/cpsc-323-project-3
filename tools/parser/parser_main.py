from .parser_data import *
from .tree import *

# Change this from True/False to enable/disable debug log
DEBUG = False


def debug_print(message):
    if DEBUG:
        print(message)


def parser(token_stream):
    input = token_stream

    if not input:
        return

    input.append("$")
    debug_print(f"Start:\n{input}\n")

    stack = [0]
    cst_stack = []
    input_index = 0

    # debug_print(f"Beginning Stack: {stack}")

    while True:
        current_state = stack[-1]
        
        current_token = input[input_index][0] # outputs tuple

        if current_token == "$":
            current_value = None  # Avoid counting the delimiter
        else:
            if len(input[input_index]) < 2:
                print(f"Error: Token at index {input_index} does not follow the tuple form: {input[input_index]}")
                return
            current_value = input[input_index][1]


        debug_print(f"Current token: {current_token} with value {current_value}")

        action = table[current_state][table_column.index(current_token)]
        debug_print(f"Action: {action}")

        if action is None:
            print("----------ERROR----------")
            print(
                f"Unexpected token '{current_token}' at index {input_index} of {input}\n")
            print(f"Current Stack: {stack}\n")
            print(f"Remaining Input: {input[input_index:]}")
            print("-------------------------")
            return

        if action.startswith('S'):
            state_to_shift = int(action[1:])
            stack.append(current_token)
            stack.append(state_to_shift)

            # Add CST leaf node
            cst_stack.append(tree_node(current_token))

            input_index += 1
            debug_print(f"Shifted Stack: {stack}\n")

        elif action.startswith('R'):
            production_index = int(action[1:])
            lhs, rhs = productions[production_index]
            debug_print(
                f"Reducing using rule {production_index}: {lhs} -> {' '.join(rhs)}")

            # Pop twice for each symbol in RHS (symbol + state)
            for _ in range(len(rhs) * 2):
                stack.pop()

            # Get new current state
            new_state = stack[-1]
            goto_state = table[new_state][table_column.index(lhs)]
            stack.append(lhs)
            stack.append(int(goto_state))
            debug_print(f"Reduced Stack: {stack}\n")

            # Create CST node
            num_children = len(rhs)
            children = cst_stack[-num_children:]
            del cst_stack[-num_children:]

            new_node = tree_node(lhs)
            
            # Adding the info based on the production symbol
            if lhs == 'A':
                var_type = rhs[0]
                new_node.semantic_info = {'var_type': var_type}
            elif lhs == 'F':
                # debug_print(f"rhs: {rhs}")
                # debug_print(f"rhs length: {len(rhs)}")
                if len(rhs) == 3:
                    first_val = input[input_index-3][1]
                    second_val = input[input_index-2][1]
                    third_val = input[input_index-1][1]

                    float_val = f"{first_val}{second_val}{third_val}"
                    new_node.semantic_info = {'var_value': float_val} # Turn into float
                elif rhs[0] == 'integer':
                    int_val = input[input_index-1][1]
                    new_node.semantic_info = {'var_value': int_val} # Turn into integer
                else:
                    var_name = input[input_index-1][1]
                    new_node.semantic_info = {'var_name': var_name}
            elif lhs == 'M':
                new_node.semantic_info = {'function_name': 'main', 'return_type': 'int'}
            elif lhs == 'R':
                return_type = children[1]
                print(f"Return node: {return_type.element}, info: {return_type.semantic_info}")
                var_type = input[input_index-2][0] # fix this
                new_node.semantic_info = {'var_type': var_type}
                            
            for child in children:
                new_node.add_child(child)

            cst_stack.append(new_node)

        elif action == "Acc":
            debug_print("Parsing successful. Accepting input.\n")
            debug_print("Concrete Syntax Tree:")
            if cst_stack:
                return cst_stack[0]
            else:
                print("CST is empty.")
            break
        

