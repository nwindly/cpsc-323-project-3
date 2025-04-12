from tools.lex.lex_main import lexer
from tools.parser.parser_main import parser

def main():
    token_stream = lexer("./test_cases/1.in")

    # Creates input.in file for the parser to read
    parser_input = ' '.join(token_stream)
    with open('parser_input.in', 'w') as file:
        file.write(parser_input)

    parser("./parser_input.in")

if __name__ == "__main__":
    main()