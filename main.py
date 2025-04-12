from tools.lex.lex_main import lexer

def main():
    token_stream = lexer("./test_cases/1.in")
    print(token_stream)

if __name__ == "__main__":
    main()