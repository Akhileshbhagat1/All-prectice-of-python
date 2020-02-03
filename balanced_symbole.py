class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


def match_symbols(symbol_str):
    symbol_pairs = {
        '(': ')',
        '{': '}',
        '[': ']',
        }
    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else:   # the symbol is a closer

                # if the stack is already empty, the symbol are not balanced
            if my_stack.is_empty():
                return False
                # if there are still items in the stack, check for a miss match
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if my_stack.is_empty():
        return True
    return False  # stack is not empty so symbols were not balanced


symbole = input('Enter your symbole here "( or { or [ or ) or } or ]" : ')
print(match_symbols(symbole))
# print(match_symbols('(([{}]])'))
# print(match_symbols('[()]'))

            

