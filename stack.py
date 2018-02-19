class Stack(object):
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        if len(self.stack) ==0:
            return True
        else:
            return False
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        data=self.stack[-1]
        del self.stack[-1]
        return data
    def peek(self):
        return self.stack[-1]
    def sizeStack(self):
        return len(self.stack)

stack=Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.sizeStack())
print(stack.peek())
