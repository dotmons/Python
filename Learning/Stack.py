class Stack:
    def __init__(self):
        self.stack = []
        self.size: int = 0

    
    def pop(self) -> int:
        if self.size>0:
            firststack = self.stack[0]
            self.stack = self.stack[1:]
            self.size -= 1
            return firststack
        return -1
    
    def push(self, value: int):
        self.stack.append(value)
        #self.stack.insert(0,value)
        self.size += 1

    def peek(self) -> int:
        if self.size>0:
            return self.stack[0]


    def is_empty(self) -> bool:
        if (self.size>0):
            return False

        return True


    def sizestack(self) -> int:
        return self.size
    
    
    def clear(self):
        self.stack.clear()

    def print_stack(self):
        for st in self.stack:
            print(st)



s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop())      # Output: 30
print(s.peek())     # Output: 20
print(s.sizestack())     # Output: 2
print(s.is_empty()) # Output: False
s.print_stack()     # Output: [10, 20]