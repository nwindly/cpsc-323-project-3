from tools.parser.parser_main import *

# class SemanticAnalyzer:
#     def __init__(self, nodes):
#         self.nodes = nodes
#         self.symbol_table = {}  
#         self.identifier_counter = 1
#         self.identifier_map = {}  # index to unique identifier names (id1, id2, etc.)
#         self.declared = set()  # Track declared variables
#         self.assigned = set()  # Track assigned variables
#         self.undeclared_but_used = set() # Track undeclared variables that have been used

#     def get_identifier_name(self, index, is_declared=False):
#         if is_declared:
#             if index not in self.identifier_map:
#                 self.identifier_map[index] = f"id{self.identifier_counter}"
#                 self.identifier_counter += 1
#             return self.identifier_map[index]
#         elif index in self.identifier_map:
#             return self.identifier_map[index]
#         return None

#     def analyze(self): 
        
#         print("\nPrinting a flat list of CST nodes:")
#         for i, node in enumerate(self.nodes):
#             print(f"Node {i}: element = {node.element}, semantic_info = {node.semantic_info}")
        
#         i = 0
#         declared_count = 0  # Tracking number of identifiers declared - can delete

#         while i < len(self.nodes):
#             # Variable type declaration: A -> type, F -> identifier
#             if (
#                 i + 3 < len(self.nodes)
#                 and self.nodes[i].element == 'A'
#                 and self.nodes[i+1].element in ['int', 'float', 'bool']
#                 and self.nodes[i+2].element == 'F'
#                 and self.nodes[i+3].element == 'identifier'
#             ):
#                 var_type = self.nodes[i+1].element
#                 var_name = self.get_identifier_name(i+3, is_declared=True)
#                 self.symbol_table[var_name] = {'type': var_type, 'value': None}  # Variable and value in the symbol table (Cannot access literal values)
#                 self.declared.add(var_name)
#                 declared_count += 1
#                 i += 4

#                 # Handle assignment (=) using the node output
#                 if i + 4 < len(self.nodes) and self.nodes[i].element == 'assignment':
#                     assigned_value = self.nodes[i+3].element 
#                     value = None
#                     assigned_type = None

#                     # Handle case where we see "true" after =
#                     if (self.nodes[i+3].element == 'integer' and
#                           self.nodes[i+4].element == 'dot' and
#                           self.nodes[i+5].element == 'integer'):
#                         # Assigned_value is not a literal value but a string of the node pattern (integer dot integer)
#                         assigned_value = f"{self.nodes[i+3].element} {self.nodes[i+4].element} {self.nodes[i+5].element}"
#                         value = assigned_value
#                         assigned_type = 'float'
#                     # Handle case for integer as integer value
#                     elif assigned_value == 'integer':
#                         value = 'integer'
#                         assigned_type = 'integer'
#                     # Handle case for "integer dot integer" which means a float value
#                     elif assigned_value == 'true' or assigned_value == 'false':
#                         value = assigned_value == 'true'
#                         assigned_type = 'bool'

#                     # Type checking requirement
#                     if var_type == 'float' and assigned_type == 'integer':
#                         assigned_type = 'Error: Float variable is assigned to an integer value.'
#                     elif var_type == 'float' and assigned_type == 'bool':
#                         assigned_type = 'Error: Float variable is assigned to a boolean.'
#                     elif var_type == 'integer' and assigned_type == 'bool':
#                         assigned_type = 'Error: Integer variable is assigned to a boolean.'
#                     elif var_type == 'integer' and assigned_type == 'float':
#                         assigned_type = 'Error: Integer variable is assigned to a float value.'
#                     elif var_type == 'bool' and assigned_type == 'integer':
#                         assigned_type = 'Error: Boolean variable is assigned to an integer value.'
#                     elif var_type == 'bool' and assigned_type == 'float':
#                         assigned_type = 'Error: Boolean variable is assigned to a float value.'

#                     # Update symbol table if value is assigned
#                     if value is not None:
#                         self.symbol_table[var_name]['value'] = value
#                         self.symbol_table[var_name]['assigned_value_type'] = assigned_type
#                         self.assigned.add(var_name)
            
#                     i += 6
                
#                 continue
            
#             if self.nodes[i].element == 'identifier':
#                 var_name = self.nodes[i].element
#                 if var_name not in self.declared:
#                     self.undeclared_but_used.add(var_name)
            
#             # Handling mixed-mode expressions - cannot do mixed-mode in this project!
#             # ...
            
#             # Handling type checking for return types
#             # ...
#             i += 1

#         # Print symbol table information
#         print("Symbol Table:\n")
#         for var_name, info in self.symbol_table.items():
#             # Value is not literal value but is the pattern that references its value (because not enough time to edit lexer and parser to store token value and token name)
#             if info['value'] is not None:
#                 print(f"{var_name}: {info['type']} = {info['value']} ({info['assigned_value_type']})")
#             else:
#                 print(f"{var_name}: {info['type']} (no value assigned)")
        
#         # Printing use before declaration error
#         if self.undeclared_but_used:
#             print("\nError: These variables that were used before declaration are:")
#             for var_name in self.undeclared_but_used:
#                 print(f"{var_name} at node ...")
        
#         # Checks for declaration correctness - can delete
#         if declared_count > 0:
#             print(f"\n{declared_count} identifiers successfully declared.")
#         else:
#             print("\nNo identifiers declared.")

class SemanticAnalyzer:
    def __init__(self, nodes):
        self.nodes = nodes
        self.symbol_table = {} # Symbol table!!!
        self.identifier_map = {}
        self.identifier_counter = 1 # For id1, id2, ...
        self.declared = set() # Track declared variables
        self.undeclared_but_used = set() # Track undeclared but used variables

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
        if isinstance(val, str):
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
        # Making sure that the node has semantic_info and 'var_value' or 'var_name'
        # Helpful for declaration before use
        if node.semantic_info:
            print(f"Node: {node}")
            if 'var_value' in node.semantic_info:
                print(f"Found var_value: {node.semantic_info['var_value']} for a node.")
            elif 'var_name' in node.semantic_info:
                var_name = node.semantic_info['var_name']
                if var_name not in self.declared:
                    self.undeclared_but_used.add(var_name)
                    print(f"Warning: {var_name} is used but not declared.")    
    
    # Analyzing the nodes based on the patterns of the flat CST nodes
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
                            print(f"\nTypeChecking Error: Cannot assign {assigned_type} to {declared_type} for variable '{var_name}'!")
                        else:
                            self.symbol_table[var_name]['value'] = value_str
                            self.symbol_table[var_name]['assigned_type'] = assigned_type
                            value_node.semantic_info.update({
                                'assigned_value': value_str,
                                'assigned_type': assigned_type
                            })
                    else:
                        print(f"\nTypeChecking Error: Could not locate value node to assign to variable '{var_name}'!")

                    i += 4  # Skip to next after assignment

                continue

            # Handle identifier usage
            if node.element == 'identifier':
                var_name = self.get_identifier_name(i)
                if var_name not in self.declared:
                    self.undeclared_but_used.add(var_name)

            # Handle mixed-mode expressions
            #...

            # Handling type checking for return types
            # ...
            
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
                print(f" - {var}!")
