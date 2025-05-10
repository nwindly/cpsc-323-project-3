from tools.lexer.lexer_main import lexer
from tools.parser.parser_main import *
from tools.semantic_analyzer.semantic import *


def main():
    """
    REFLECTION FOR PROJECT 3:

        Our lexer produces a token stream as an array, such as:
        ['int', 'main', 'leftParen', 'rightParen', 'leftBrace', 'int', 'identifier', ...].

        Our parser uses this array and eventually produces an array of nodes, applying production rules and using a parsing table.

        Our semantic analyzer takes this array as input and should have performed semantic analysis but it failed.

        Reason why our semantic analyzer did not work:
            - We did not include the value of each token.
                For example, the input to the semantic analyzer was an array of tokens like:
                [P, B, A, int, M, main, leftParen, rightParen, B, leftBrace, ..., identifier, ...].
                With this format, even if we build a symbol table and try to store types and identifier names, the semantic analyzer cannot tell 
                which identifier is being referenced because it only sees the generic label "identifier".

        If we had designed the lexer to produce not only token types but also include their values, such as variable names or literal values,
        the semantic analyzer would have been able to track declarations and usages properly.

        Looking back, we should have designed our lexer to produce not only token types but also their associated values.
        This would have allowed the semantic analyzer to properly track declarations, usages, and perform type checking.

        Unfortunately, we have found out about this issue too late. Even though our project is incomplete, we've learned a lot about how to 
        communicate with other team members and work together as a team. We also learned about how complicated compilers are, with many 
        implementations and details to be appreciated. We tried our best to finish this project, but was not able to do it on time.
        However, we are grateful for the opportunity to learn from this experience.

    """

    token_stream = lexer("./test_cases/1.in")

    tree = parser(token_stream)
    nodes = tree.get_all_nodes()

    if tree:
        tree.print_tree()

    # index = 0
    # for node in nodes:
    #     print(f"{index}: {node}")
    #     index = index + 1
    # print("---------------")

    semantic = SemanticAnalyzer(tree.get_all_nodes())
    # semantic = SemanticAnalyzer(nodes)
    semantic.analyze()


if __name__ == "__main__":
    main()
