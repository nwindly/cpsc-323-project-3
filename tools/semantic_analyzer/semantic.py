class SemanticAnalyzer:
    def __init__(self, nodes):
        self.nodes = nodes
        self.symbol_table = {}
        self.identifier_counter = 1
        self.identifier_map = {}  # index to identifier names (id1, id2, etc..)
        self.declared = set()
        self.assigned = set()

    def get_identifier_name(self, index):
        if index not in self.identifier_map:
            self.identifier_map[index] = f"id{self.identifier_counter}"
            self.identifier_counter += 1
        return self.identifier_map[index]

    def analyze(self):
        i = 0
        while i < len(self.nodes):
            # Variable declaration: A -> type, F -> identifier
            if self.nodes[i].element == 'A':
                var_type = self.nodes[i+1].element
                if self.nodes[i+2].element == 'F' and self.nodes[i+3].element == 'identifier':
                    var_name = self.get_identifier_name(i+3)
                    print(f"var_name: {var_name}")
                    self.symbol_table[var_name] = var_type
                    i += 4
                    continue

            # TODO: Assignment: F identifier = T or literal

            # Variable declaration or use
            elif self.nodes[i].element == 'F' and self.nodes[i+1].element == 'identifier':
                var_name = self.get_identifier_name(i+1)
                if var_name not in self.declared:
                    print(f"Error! The variable '{var_name}' was used before declaration.")
                elif var_name not in self.assigned:
                    print(f"Error! The variable '{var_name}' was used before it was assigned a value.")
                i += 2
                continue
            
            i += 1

        print("\nSymbol Table:")
        for k, v in self.symbol_table.items():
            print(f"{k}: {v}")
