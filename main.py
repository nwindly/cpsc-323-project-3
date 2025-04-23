from tools.lexer.lexer_main import lexer
from tools.parser.parser_main import *


def main():
    token_stream = lexer("./test_cases/1.in")
    tree = parser(token_stream)
    nodes = tree.get_all_nodes()

    # IMPORTANT: element of nodes is a tree object. When using Print(element), it will print the value. However,
    # the value's type is NOT string. It is a tree object type. Therefore, we need to typecast it to String everytime
    # we want to do any calculations and comparisons.
    # EXAMPLE:
    # x = nodes[0]
    # print("P"== str(x))
    # print(type(x))
    # print(x)

    index = 0
    for i in nodes:
        print(f"{index}: {i}")
        index = index + 1



    

if __name__ == "__main__":
    main()
