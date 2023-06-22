class Stack:
    def __init__(self, stack=[]):
        self.stack = stack 

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        try:
            return self.stack.pop(-1)
        except IndexError as er:
            return f'Элементов в stack больше нет. Он пуст.'
        
    def peek(self):
        try:
            return self.stack[-1]
        except IndexError as er:
            return f'Элементов в stack нет. Он пуст.'
        
    def size(self):
        return(len(self.stack))
    
    def is_balance_brackets(self, brackets_text:str):
        for bracket in brackets_text:
            if bracket in ['(', '[', '{']:
                self.push(bracket)
            elif bracket in ['}', ']', ')']:
                if self.isEmpty == True:
                    return False
                bracket_r = self.pop()
                if not ((bracket_r == '{' and bracket == '}')
                    or (bracket_r == '[' and bracket == ']')
                    or (bracket_r == '(' and bracket == ')')):
                    return False
        return  self.isEmpty()


if __name__ == "__main__":
    b = Stack()
    print(b.is_balance_brackets('[[{())}]'))
    # s = Stack()
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # print(s.size())
    # print(s.pop())
    # print(s.peek())
    # print(s.pop())
    # print(s.peek())
    # print(s.size())
    # print(s.peek())
    

