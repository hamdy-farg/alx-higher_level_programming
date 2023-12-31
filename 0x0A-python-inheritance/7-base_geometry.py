#!/usr/bin/python3
""" creating a class """


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        area method
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value): 
        """ function to validate an iteger"""
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        elif(value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
