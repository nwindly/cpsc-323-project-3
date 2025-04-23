from tools.lexer.lexer_main import lexer
from tools.parser.parser_main import *


def main():
    token_stream = lexer("./test_cases/1.in")
    tree = parser(token_stream)
    nodes = tree.get_all_nodes()
    index = 0
    for node in nodes:
        print(f"{index}: {node}")
        index = index + 1



    

if __name__ == "__main__":
    main()
