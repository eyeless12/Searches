def simple_search(substring, string):
    left_border = 0
    right_border = len(substring) - 1
    while right_border < len(string):
        if string[left_border:right_border] == substring:
            return left_border
        left_border += 1
        right_border += 1
        return -1