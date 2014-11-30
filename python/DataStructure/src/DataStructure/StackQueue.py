class Stack(object):
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack==[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            raise IndexError,'pop from empty stack'
        return self.stack.pop()
    def size(self):
        return len(self.stack)
class Queue_with_stacks(object):
    def __init__(self):
        self.stackA=Stack()
        self.stackB=Stack()
    def isEmpty(self):
        return self.stackA.isEmpty() and self.stackB.isEmpty()
    def enqueue(self,item):
        self.stackA.push(item)
    def dequeue(self):
        if self.stackB.isEmpty():
            if self.stackA.isEmpty():
                raise IndexError,'queue is empty.'
            while self.stackA.size()>=2:
                self.stackB.push(self.stackA.pop())

            return self.stackA.pop()
        else:
            return self.stackB.pop()