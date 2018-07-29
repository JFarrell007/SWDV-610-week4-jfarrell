"""
Name: Jim Farrell
Description: Implement a deque using linked lists

Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the deque. It needs no parameters and returns an integer.

"""
from node import *
from empty_error import *

class Deque:
    
    def __init__(self):
        """Create an empty deque."""
        self.head = None
        self.tail = None
        self.count = 0
    
    def addRear(self, val):
        """adds node to rear of deque"""
        newNode = Node(val)
        #handle the first item in the deque
        if self.isEmpty():
            newNode.setPrev(None)#set the prev node to None
            newNode.setNext(None)#set the next node to None
            self.head = newNode#assign the new node to the head of the deque
            self.tail = self.head#the tail is also the head since there is only one node
        else:#there is at least one node already in dequeue
            newNode.setNext(None)#set the last node next to None
            self.tail.setNext(newNode)#point the current tail node next to the new node
            newNode.setPrev(self.tail)#point the new node prev to the existing tail node
            self.tail = newNode#the new node now becomes the tail of the deque
        self.count += 1#increment the count
        
    def addFront(self, val):
        """adds node to front of deque"""
        newNode = Node(val)
        #handle the first item in the queue
        if self.isEmpty():
            newNode.setPrev(None)#set the prev node to None
            newNode.setNext(None)#set the next node to None
            self.head = newNode#assign the new node to the head of the deque
            self.tail = self.head#the tail is also the head since there is only one node
        elif self.tail.getPrev() == None:#handle case of one node in deque
            #self.tail = self.head#The new tail becomes the 
            self.tail.setPrev(newNode)#point tail node prev to new node
            newNode.setNext(self.tail)#point new node next to the tail node
            newNode.setPrev(None)#set the new node prev to None
            self.head = newNode#assign the new node to the head of the deque
        else:#more than one nodes in dequeu
            newNode.setNext(self.head)#point the new node next to the head of deque
            newNode.setPrev(None)#set the new node prev to None
            self.head.setPrev(newNode)#point the current head prev to new node
            self.head = newNode#set the head to the new node
            
        self.count += 1

    def removeFront(self):
        """removes node from front of deque"""
        #check for empty deque
        if self.isEmpty():#
            try:
                #raise exception when trying to remove from an empty deque
                raise EmptyError('cannot remove item from empty deque')
            #catch the error and print a message
            except EmptyError as err:
                print("Deque error removeFront(): ", err)
            return "deque is empty"
        #handle the case of only one node in the deque
        elif self.head.getNext() == None:
            self.head = None
            self.count -= 1
        else:#more than one node in deque
            #point the head to the next node
            self.head = self.head.getNext()
            self.count -= 1
    
    def removeRear(self):
        """removes node from rear of deque"""
        #check for empty deque
        if self.isEmpty():
            try:
                #raise exception when trying to remove from an empty deque
                raise EmptyError('cannot remove item from empty deque')
            #catch the error and print a message
            except EmptyError as err:
                print("Deque error removeRear(): ", err)
            return "deque is empty"
        else:
            #point the second to the last node in deque to None
            self.tail.getPrev().setNext(None)
            #set the tail to None
            self.tail = None
    
    def isEmpty(self):
        """method to check for an empty deque"""
        #if the head of the deque is set to None or Null then it is empty
        if self.head == None:
            return True
        
    def size(self):
        """method to return the size of the deque"""
        return self.count
        
    def printList(self):
        """method to print items in the deque"""
        curNode = self.head
        while curNode:
            print(curNode.getValue())
            curNode = curNode.getNext()
                       
def testIt():
    """method to test the functionality of Deque"""
    theDeque = Deque()
    
    print("adding 6 - 10 to rear of deque")
    for i in range(6,11):
        theDeque.addRear(i)
    theDeque.printList()
    print("The size of deque is {}".format(theDeque.size()))
    print("adding 1 - 5 to front of deque")
    for i in range(5,0,-1):
        theDeque.addFront(i)
    theDeque.printList()
    print("The size of deque is {}".format(theDeque.size()))
    print("Removing first 5 items from front of deque")
    for i in range(0,5):
        theDeque.removeFront()
    theDeque.printList()
    print("The size of the deque is {}".format(theDeque.size()))
    print("Removing the remaining items from the rear of the deque")
    for i in range(0,theDeque.size()):
        theDeque.removeFront()
    theDeque.printList()
    print("The size of the deque is {}".format(theDeque.size()))
    print("Try to remove from an empty deque")
    theDeque.removeFront()
    theDeque.removeRear()

testIt()
    
    