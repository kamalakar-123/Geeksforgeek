class myStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if self.stack:
            self.stack.pop()
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return -1
    
    def getSize(self):
        return len(self.stack)
    
    def isEmpty(self):
        return len(self.stack) == 0