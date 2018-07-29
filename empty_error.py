"""
Name: Jim Farrell
Description: class to handle exceptions when trying to delete from empty structures
"""

class Error(Exception):
    """Base class for exceptions in this module"""
    pass

class EmptyError(Error):
    """Raised when an empty is structure accessed"""
    
    def __init__(self, message):
        self.message = message
    