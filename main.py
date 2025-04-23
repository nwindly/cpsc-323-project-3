from tools.lexer.lexer_main import lexer
from tools.parser.parser_main import *

def main():
    token_stream = lexer("./test_cases/3.in")

    tree = parser(token_stream)
    nodes = tree.get_all_nodes()
    for i in nodes:
        print(i)

if __name__ == "__main__":
    main()