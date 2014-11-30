class Queue(object):
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        if self.queue:
            a=self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError,'queue is empty'
    def size(self):
        return len(self.queue)
class Stack_with_queues(object):
    def __init__(self):
        self.queueA=Queue()
        self.queueB=Queue()
    def isEmpty(self):
        return self.queueA.isEmpty() and self.queueB.isEmpty()
    def push(self,item):
        if self.queueB.isEmpty():
            self.queueA.enqueue(item)
        else:
            self.queueB.enqueue(item)
    def pop(self):
        if self.isEmpty():
            raise IndexError,'stack is empty'
        elif self.queueB.isEmpty():
            while not self.queueA.isEmpty():
                cur=self.queueA.dequeue()
                if self.queueA.isEmpty():
                    return cur
                self.queueB.enqueue(cur)
        else:
             while not self.queueB.isEmpty():
                cur=self.queueB.dequeue()
                if self.queueB.isEmpty():
                    return cur
                self.queueA.enqueue(cur)