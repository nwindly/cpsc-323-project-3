from tools.lexer.lexer_main import lexer
from tools.parser.parser_main import parser

def main():
    token_stream = lexer("./test_cases/1.in")

    parser(token_stream)

if __name__ == "__main__":
    main()