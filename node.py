"""
Name: Jim Farrell
Description: Node class used by all three examples
"""

class Node:
    
    def __init__(self, val):
        """constructor"""
        self.val = val#value store in node
        self.next = None#pointer to next node in list
        self.prev = None# points to previous node in list. only used in deque
    
    def setValue(self, val):
        """method to assign value to node"""
        self.val = val
        
    def getValue(self):
        """method to get value from node"""
        return self.val
    
    def getNext(self):
        """method to return the next node pointer"""
        return self.next
    
    def setNext(self, next):
        """method to assign pointer to next node"""
        self.next = next
    
    def getPrev(self):
        """method to return previous node pointer"""
        return self.prev
    
    def setPrev(self, prev):
        """method to assign pointer to prevous node"""
        self.prev = prev
