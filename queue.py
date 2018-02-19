class Queue(object):
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        data=self.queue[0]
        del self.queue[0]
        return data
    def peek(self):
        return self.queue[0]
    def sizeQueue(self):
        return len(self.queue)
queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.isEmpty())
queue.dequeue()
queue.dequeue()
queue.dequeue()

print(queue.sizeQueue())
print(queue.peek())
