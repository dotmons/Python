import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.size: int = 0
        self.min: int = sys.maxsize

    
    def pop(self) -> int:
        if self.size>0:
            laststack = self.stack[self.size-1]
            self.stack = self.stack[:self.size-1]
            self.size -= 1
            return laststack
        return -1
    
    def push(self, value: int):
        self.stack.append(value)
        self.size += 1
        self.min = min(self.min, value)

    def peek(self) -> int:
        return self.stack[self.size-1]


    def is_empty(self) -> bool:
        if (self.size>0):
            return False

        return True


    def sizestack(self) -> int:
        return self.size
    
    
    def clear(self):
        self.stack.clear()

    def print_stack(self):
        for st in reversed(self.stack):
            print(st)

    def getMin(self):
        return self.min



s = Stack()
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.getMin())
s.push(1)
print(s.getMin())
