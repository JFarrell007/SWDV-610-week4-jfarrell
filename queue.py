"""
Name: Jim Farrell
Description: Implement a queue using linked lists
FIFO
Queue() creates a new queue
enqueue(item) adds a new item to the rear of the queue
deque() removes the front item from the queue
isEmpty() tests to see whether the queue is empty
size() returns the number of items in the queue
"""
from node import *
from empty_error import *

class Queue:
    
    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self.count = 0
            
    def enqueue(self, val):
        """method to add node to the end of the queue."""
        
        newNode = Node(val)#create the new node
        #handle the first node in the queue
        if self.isEmpty():
            self.head = newNode#just set the head to the new node
        else:#queue has items
            #point the tail to the new node
            self.tail.setNext(newNode)
        #set the tail of the queue to point to the new node
        self.tail = newNode
        self.count += 1
        
    def dequeue(self):
        """method to remove node from front of queue"""
        if self.isEmpty():#
            try:
                #raise exception when trying to remove from an empty queue
                raise EmptyError('cannot remove item from empty deque')
            #catch the error and print a message
            except EmptyError as err:
                print("queue error dequeue(): ", err)  
            return "queue is empty"
            
        value = self.head.getValue()#get value from head of queue
        self.head = self.head.getNext()#point the head to the next node in queue
        self.count -= 1
 
        return value
        
    def peek(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty. """
        if self.isEmpty():
            return "Stack is empty"
        return self.head.val #top of stack is at head of list

    def size(self):
        """method that returns size of the queue"""
        return self.count
    
    def isEmpty(self):
        """method to check for an empty queue"""
        #if the head of the queue is set to None or Null then it is empty
        if self.head == None:
            return True
        
    def printList(self):
        """method to print items in the queue"""
        curNode = self.head
        while curNode:
            print(curNode.getValue())
            curNode = curNode.getNext()

def testIt():
    """method to test queue functionality"""
    
    theQ = Queue()
    print("adding values 0 - 9 to the queue")
    for i in range(10):
        theQ.enqueue(i)
    theQ.printList()
    print("the size of the queue is {}".format(theQ.size()))
    print("removing 5 oldest nodes from queue")
    for i in range(5):
        theQ.dequeue()
    print("items remaining")
    theQ.printList()
    print("the size of the list is {}".format(theQ.size()))
    print("removing the rest of the nodes from queue")
    for i in range(theQ.size()):
        theQ.dequeue()
    theQ.printList()
    print("the size of the list is {}".format(theQ.size()))
    print("try to remove from an empty queue")
    theQ.dequeue()
    
testIt()