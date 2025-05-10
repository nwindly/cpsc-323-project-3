class SemanticAnalyzer:
    def __init__(self, nodes):
        self.nodes = nodes
        self.symbol_table = {}  # Maps variable to its type and assigned value
        self.identifier_counter = 1
        self.identifier_map = {}  # Maps index to unique identifier names (id1, id2, etc.)
        self.declared = set()  # Keeps track of declared variables
        self.assigned = set()  # Keeps track of assigned variables
        self.undeclared_but_used = set() # Keeps track of undeclared variables that have been used

    def get_identifier_name(self, index, is_declared=False):
        # Id assigned only during declaration
        if is_declared:
            if index not in self.identifier_map:
                self.identifier_map[index] = f"id{self.identifier_counter}"
                self.identifier_counter += 1
            return self.identifier_map[index]
        elif index in self.identifier_map:
            return self.identifier_map[index]
        return None

    def analyze(self): 
        i = 0
        declared_count = 0  # Tracking number of identifiers declared - can delete

        while i < len(self.nodes):
            # Variable type declaration: A -> type, F -> identifier
            if (
                i + 3 < len(self.nodes)
                and self.nodes[i].element == 'A'
                and self.nodes[i+1].element in ['int', 'float', 'bool']
                and self.nodes[i+2].element == 'F'
                and self.nodes[i+3].element == 'identifier'
            ):
                var_type = self.nodes[i+1].element
                var_name = self.get_identifier_name(i+3, is_declared=True)
                self.symbol_table[var_name] = {'type': var_type, 'value': None}  # Variable and value in the symbol table (Cannot access literal values)
                self.declared.add(var_name)
                declared_count += 1
                i += 4

                # Handle assignment (=) using the node output
                if i + 4 < len(self.nodes) and self.nodes[i].element == 'assignment':
                    assigned_value = self.nodes[i+3].element 
                    value = None
                    assigned_type = None

                    # Handle case where we see "true" after =
                    if (self.nodes[i+3].element == 'integer' and
                          self.nodes[i+4].element == 'dot' and
                          self.nodes[i+5].element == 'integer'):
                        # Assigned_value is not a literal value but a string of the node pattern (integer dot integer)
                        assigned_value = f"{self.nodes[i+3].element} {self.nodes[i+4].element} {self.nodes[i+5].element}"
                        value = assigned_value
                        assigned_type = 'float'
                    # Handle case for integer as integer value
                    elif assigned_value == 'integer':
                        value = 'integer'
                        assigned_type = 'integer'
                    # Handle case for "integer dot integer" which means a float value
                    elif assigned_value == 'true' or assigned_value == 'false':
                        value = assigned_value == 'true'
                        assigned_type = 'bool'

                    # Type checking requirement
                    if var_type == 'float' and assigned_type == 'integer':
                        assigned_type = 'Error: Float variable is assigned to an integer value.'
                    elif var_type == 'float' and assigned_type == 'bool':
                        assigned_type = 'Error: Float variable is assigned to a boolean.'
                    elif var_type == 'integer' and assigned_type == 'bool':
                        assigned_type = 'Error: Integer variable is assigned to a boolean.'
                    elif var_type == 'integer' and assigned_type == 'float':
                        assigned_type = 'Error: Integer variable is assigned to a float value.'
                    elif var_type == 'bool' and assigned_type == 'integer':
                        assigned_type = 'Error: Boolean variable is assigned to an integer value.'
                    elif var_type == 'bool' and assigned_type == 'float':
                        assigned_type = 'Error: Boolean variable is assigned to a float value.'

                    # Update symbol table if value is assigned
                    if value is not None:
                        self.symbol_table[var_name]['value'] = value
                        self.symbol_table[var_name]['assigned_value_type'] = assigned_type
                        self.assigned.add(var_name)
            
                    i += 6
                
                continue
            
            if self.nodes[i].element == 'identifier':
                var_name = self.nodes[i].element
                if var_name not in self.declared:
                    self.undeclared_but_used.add(var_name)
            
            # Handling mixed-mode expressions - cannot do mixed-mode in this project!
            # ...
            
            # Handling type checking for return types
            # ...
            i += 1

        # Print symbol table information
        print("Symbol Table:\n")
        for var_name, info in self.symbol_table.items():
            # Value is not literal value but is the pattern that references its value (because not enough time to edit lexer and parser to store token value and token name)
            if info['value'] is not None:
                print(f"{var_name}: {info['type']} = {info['value']} ({info['assigned_value_type']})")
            else:
                print(f"{var_name}: {info['type']} (no value assigned)")
        
        # Printing use before declaration error
        if self.undeclared_but_used:
            print("\nError: These variables that were used before declaration are:")
            for var_name in self.undeclared_but_used:
                print(f"{var_name} at node ...")
        
        # Checks for declaration correctness - can delete
        if declared_count > 0:
            print(f"\n{declared_count} identifiers successfully declared.")
        else:
            print("\nNo identifiers declared.")

