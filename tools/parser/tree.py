# Class to make a list of tree nodes

class tree_node:
    def __init__(self, element, semantic_info=None):
        self.element = element
        # Initialize a list of children for this node
        self.children = []
        self.semantic_info = semantic_info # To add info in parse tree for semantic analysis

    def add_child(self, node):
        self.children.append(node)

    # Func has spaces argument for it to be recursive
    def print_tree(self, spaces="", last_node=True):
        if (last_node):
            connection = "└── "
        else:
            connection = "├── "

        line = spaces + connection + self.element
        # Print info into the parse tree
        if self.semantic_info:
            line += f" (info: {self.semantic_info})"
        else:
            line += " (No info.)"
        print(line)

        if (last_node):
            spaces += "    "
        else:
            spaces += "│   "

        # Now call recursively to print all subtrees
        counter = 0
        for child_node in self.children:
            # Check if child node is last node
            if (counter >= (len(self.children) - 1)):
                last_node = True
            else:
                last_node = False

            child_node.print_tree(spaces, last_node)
            counter += 1

    # Prints an array of node objects
    def get_all_nodes(self):
        nodes = [self]  # Start with the current node
        for child in self.children:
            # Recursively add all child nodes
            nodes.extend(child.get_all_nodes())
        return nodes

    def __str__(self):
        return self.element

    
