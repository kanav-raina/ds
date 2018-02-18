class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
    def insertStart(self,data):
        self.size=self.size+1
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode
    #O(1)
    def size1(self):
        return self.size
    #O(n)
    def size2(self):
        actualNode=self.head
        size=0
        while actualNode != None:
            actualNode=actualNode.nextNode
            size=size+1
        return size
    def insertEnd(self,data):
        self.size = self.size + 1
        newNode=Node(data)
        actualNode=self.head
        while actualNode.nextNode != None:
            actualNode=actualNode.nextNode
        actualNode.nextNode=newNode
    def traverse(self):
        actualNode=self.head
        while actualNode !=None:
            print(actualNode.data)
            actualNode=actualNode.nextNode
    def remove(self,data):
        if self.head == None:
            return
        self.size=self.size-1
        currentNode=self.head
        previousNode=None
        while currentNode.data != data:
            previousNode=currentNode
            currentNode=currentNode.nextNode
        if previousNode == None:
            self.head=currentNode.nextNode
        else:
            previousNode=currentNode.nextNode
linkedlist=LinkedList()
linkedlist.insertStart(1)
linkedlist.insertStart(10)
linkedlist.insertStart(100)
linkedlist.remove(100)
linkedlist.insertEnd(1000)
linkedlist.traverse()
print(linkedlist.size1())
