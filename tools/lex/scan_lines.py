def scan_lines(filename):
    lines = []
    with open(filename) as file:
        lines = [line for line in file]
    return lines