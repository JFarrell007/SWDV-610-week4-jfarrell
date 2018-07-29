"""
Name: Jim Farrell
Description: Implement a stack using linked lists
LIFO
Stack() creates a new stack
push(item) adds a new item to the top of the stack
pop() removes the top itme from the stack
peek() returns the top item from the stack but does not remove it
isEmpty() tests to see whether the stack is empty
size() returns the number of items on the stack
"""
from node import *
from empty_error import *

class Stack:
    
    def __init__(self):
        """Create an empty stack."""
        self.head = None
        self.count = 0
                  
    def push(self, val):
        """method to add a node the top of the stack."""
        newNode = Node(val)#create the new node with val
        newNode.setNext(self.head)#set the next node to the current head
        self.head = newNode#set the head node to new node
        self.count += 1
        
    def pop(self):
        """method that removes the node from the top of the stack"""
        if self.isEmpty():#
            try:
                #raise exception when trying to remove from an empty stack
                raise EmptyError('cannot remove item from empty stack')
            #catch the error and print a message
            except EmptyError as err:
                print("stack error pop(): ", err)        
            return "Stack empty"

        value = self.head.getValue()#get the value of from the head of the stack
        self.head = self.head.getNext()#set the head of the stack to the next node in the stack
        self.count -= 1
        return value
        
    def peek(self):
        """method that returns (does not remove) the value of the top of the stack."""
        
        if self.isEmpty():#
            try:
                #raise exception when trying to remove from an empty stack
                raise EmptyError('stack is empty')
            #catch the error and print a message
            except EmptyError as err:
                print("peek():", err)        
            return "Stack empty"
        
        return self.head.val #return the value of the head of the stack
    
    def size(self):
        """method that returns size of the stack"""
        return self.count
    
    def isEmpty(self):
        """method to check for an empty stack"""
        #if the head of the stack is set to None or Null then it is empty
        if self.head == None:
            return True
        
    def printList(self):
        """method to print items in the stack"""
        curNode = self.head
        while curNode:
            print(curNode.getValue())
            curNode = curNode.getNext()


def testIt():
    """method to test functionality of stack"""
    TEST_RANGE = 10
    s = Stack()
    
    print("Stack is empty = {}".format(s.isEmpty()))
    for i in range(TEST_RANGE):
        print("Adding {} to the stack".format(i))
        s.push(i)
        print("Let's take a peek() to see whats on top {}".format(s.peek()))
    print("items on the stack are:")
    s.printList()    
    print("Stack size before starting pop()s is {}".format(s.size()))
    for i in range(TEST_RANGE ):
        print("Removing {} from the stack.".format(s.pop()))
    print("Try to remove from an empty stack")
    s.pop()
    print("Peek at top of empty stack")
    s.peek()
        
    
testIt()
