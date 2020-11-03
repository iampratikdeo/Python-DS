class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if len(self.stack) <= 0:
            return ("No element in stack")
        else:
            return self.stack.pop()


AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.pop())
print(AStack.pop())
