class Queue:
    def __init__(self):
        self.queueList = []
        self.size = 0

    def add(self, val: int):
            self.queueList.append(val)
            self.size+=1

    def remove(self):
        if self.size>0:
            del self.queueList[0]
            self.size-=1
        else:
            raise NameError("Size is Empty")

    def poll(self) -> int:
        if (self.size>0):
            firstqueue = self.queueList[0]
            self.queueList = self.queueList[1:]
            self.size -= 1
            return firstqueue
        return -1

    def element(self) -> int:
        if (self.size>0):
            return self.queueList[0]
        else:
            raise NameError("Queue is empty")
        
    
    def peek(self) -> int:
        if (self.size>0):
            return self.queueList[0]
        
        return None
    
    def print(self):
        for i in self.queueList:
            print(i)



q = Queue()
q.add(10)
q.add(20)
q.add(30)


print('Polled element: ', q.poll())
q.print()

print('Size> ',q.size)
q.remove()
print('Size> ',q.size)
q.print()