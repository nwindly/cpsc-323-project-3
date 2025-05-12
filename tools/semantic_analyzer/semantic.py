from tools.parser.parser_main import *

class SemanticAnalyzer:
    def __init__(self, nodes):
        self.nodes = nodes
        self.symbol_table = {} # Symbol table!!!
        self.identifier_map = {}
        self.identifier_counter = 1 # For id1, id2, ...
        self.declared = set() # Track declared variables
        self.undeclared_but_used = set() # Track undeclared but used variables
        self.return_type = None # Initialized to None

    # Function to retrieve the actual variable name or create the names (id1, id2, ...)
    def get_identifier_name(self, index, is_declared=False, actual_var_name=None): # Getting or creating name when is_declared is False
        if is_declared:
            if index not in self.identifier_map:
                if actual_var_name:
                        self.identifier_map[index] = actual_var_name
                else:
                    self.identifier_map[index] = f"id{self.identifier_counter}"
                    self.identifier_counter += 1
            return self.identifier_map[index]
        # If var not declared, check if it's in the map
        elif index in self.identifier_map:
            return self.identifier_map[index]
        return None

    # Function for getting the types from the values of the node
    def get_type_from_value_node(self, node, next_node=None):
        if not node.semantic_info:
            return 'unknown'

        val = node.semantic_info.get('var_value')
        if isinstance(val, str): # str, float, int, bool based on if semantic info output was converted or not
            if val in ['true', 'false']:
                return 'bool'
            elif '.' in val:
                return 'float'
            else:
                return 'int'
        elif isinstance(val, float):
            return 'float'
        elif isinstance(val, int):
            return 'int'
        elif isinstance(val, bool):
            return 'bool'
        return 'unknown'
    
    def assign_value(self, node):
        # Making sure that the node has semantic info and either var val or type
        if node.semantic_info:
            if 'var_value' in node.semantic_info:
                pass
            elif 'var_name' in node.semantic_info:
                var_name = node.semantic_info['var_name']
                if var_name not in self.declared:
                    self.undeclared_but_used.add(var_name)
                    print(f"Error: {var_name} is used but not declared.")    
    
    # Analyzing the nodes based on the patterns of the CST nodes
    def analyze(self):
        # # For debugging purposes - can delete
        # print("\nPrinting a flat list of CST nodes:")
        # for i, node in enumerate(self.nodes):
        #     print(f"Node {i}: element = {node.element}, semantic_info = {node.semantic_info}")
        i = 0
        while i < len(self.nodes):
            node = self.nodes[i]

            # Handle declaration
            if (
                i + 3 < len(self.nodes)
                and self.nodes[i].element == 'A'
                and self.nodes[i+1].element in ['int', 'float', 'bool']
                and self.nodes[i+2].element == 'F'
                and self.nodes[i+3].element == 'identifier'
            ):
                declared_type = self.nodes[i+1].element
                actual_var_name = self.nodes[i+2].semantic_info.get('var_name') # Gets the actual variable name like "myInt" instead of "id1"
                var_name = self.get_identifier_name(i+3, is_declared=True, actual_var_name=actual_var_name) # Getting name when is_declared is True
                self.symbol_table[var_name] = {'type': declared_type, 'value': None}
                self.declared.add(var_name)

                self.nodes[i+3].semantic_info = {
                    'var_name': var_name,
                    'declared_type': declared_type,
                    'is_declared': True
                }

                i += 4

                # Handle assignment after declaration
                if i + 1 < len(self.nodes) and self.nodes[i].element == 'assignment':
                    value_node = None
                    if i + 1 < len(self.nodes) and self.nodes[i+1].element == 'T':
                        t_node = self.nodes[i+1]
                        for child in t_node.children:
                            if child.element == 'F' and child.semantic_info:
                                if 'var_value' in child.semantic_info:
                                    value_node = child
                                    break
                                elif 'var_name' in child.semantic_info and child.semantic_info['var_name'] in ['true', 'false']:
                                    # Convert to boolean
                                    child.semantic_info['var_value'] = child.semantic_info['var_name']
                                    value_node = child
                                    break

                    if value_node:
                        assigned_type = self.get_type_from_value_node(value_node)
                        value_str = value_node.semantic_info.get('var_value')
                        # Type checking error
                        if declared_type != assigned_type:
                            print(f"\nTypeChecking Error! Cannot assign {assigned_type} to {declared_type} for variable '{var_name}'.")
                        else:
                            self.symbol_table[var_name]['value'] = value_str
                            self.symbol_table[var_name]['assigned_type'] = assigned_type
                            value_node.semantic_info.update({
                                'assigned_value': value_str,
                                'assigned_type': assigned_type
                            })
                    else:
                        print(f"\nTypeChecking Error: There's no value to the variable '{var_name}'.")

                    i += 4

                continue

            # Handle mixed-mode expressions
            elif self.nodes[i].element == 'plus':
                # Check the operands to the left and to the right
                if i + 1 < len(self.nodes) and i - 1 >= 0:
                    left_operand = self.nodes[i-2] # F -> identifier node
                    right_operand = self.nodes[i+2] # F -> identifier node

                    # Get the type from the operand nodes in the expression and check if types are the same
                    left_type = self.get_type_from_value_node(left_operand)
                    right_type = self.get_type_from_value_node(right_operand)

                    if left_type != right_type:
                        print(f"Mixed Mode Expression Error: Cannot add {left_type} and {right_type}.")
                    else:
                        print(f"Operands are compatible for the plus operation.")

            # Handling type checking for return types
            elif node.element == 'R':
                factor_node = node.children[0] 
                return_type = self.get_type_from_value_node(factor_node)
                self.return_type = return_type
                
                if self.return_type != 'int': 
                    print(f"TypeChecking Error: Return type '{self.return_type}' does not match 'int'.")
                i += 1

            # Handle identifier usage
            if node.element == 'identifier':
                var_name = self.get_identifier_name(i)
                if var_name not in self.declared:
                    self.undeclared_but_used.add(var_name)

            if node.element not in ['F', 'M']:
                self.assign_value(node)

            # Assign values when a 'var_value' is found in the node
            self.assign_value(node)
            i += 1

        # Print symbol table information
        print("\nSymbol Table:")
        for var, info in self.symbol_table.items():
            print(f"{var}: {info}")

        # Print when undeclared variables are used
        if self.undeclared_but_used:
            print("\nError: These variables were used before declaration:")
            for var in self.undeclared_but_used:
                print(f" - {var}")
