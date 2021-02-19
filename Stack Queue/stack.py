

class Stack:
    def __init__(self):
        if self.items == []:
            return 'empty'
        self.items = []
    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def is_empty(self):
        if self.items == []:
            return True
        return False


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.pop()
s.pop()
print(s.items)

