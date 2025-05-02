from tools.lexer.lexer_main import lexer
from tools.parser.parser_main import *
from tools.semantic_analyzer.semantic import *


def main():
    token_stream = lexer("./test_cases/1.in")
    tree = parser(token_stream)
    nodes = tree.get_all_nodes()
    index = 0
    for node in nodes:
        print(f"{index}: {node}")
        index = index + 1
    print("---------------")

    semantic = SemanticAnalyzer(nodes)
    semantic.analyze()

    """
    Reflection: 

        Our lexer produces an array of token stream, such as ['int', 'main', 'leftParen', 'rightParen', 'leftBrace', 'int', 'identifier', etc..].
        Our parser gets uses this array and eventually produces an array of nodes that contains element using production rules and table.
        Our semantic analyzer uses this array and should've produced results of semantic analysis, but failed.

        Reason for our semantic analyzer NOT working:
        -   We don't know the value of the token. 
            For example, the input for the semantic analyzer is an array of object containing only
            elements of [P, B, A, int, M, main, leftParen, rightParen, B, leftBrace, ... , identifier, etc..].
            With this input, even if we create a symbol table and store the type and id number in the table, 
            our semantic analyzer won't know which identifier already has been declared because it will read it only as
            "identifier". If we had fixed our lexer to produce not only token streams, but also provided a value such as
            a variable name or the actual value of the RHS, this would've checked which variable is being used.

        
            


    
    
    """


if __name__ == "__main__":
    main()
