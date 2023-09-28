#!/usr/bin/python3
""" bla vla bla """

class Square:
    """ square class """
    def __init__(self, size=0):
        """ small intialization """
        if (type (size)!= int):
            raise TypeError
            ("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0") 
        self.__size = size
    @property
    def size(self):
        """ size gitter """
        return self.__size

    @size.setter
    def size(self, value):
        """ this is size setter"""
        
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0") 
        self.__size = value
        
    def area(self):
        """ this area function """
        return self.__size *  self.__size
        
    def my_print(self):
        """ my print func to print num ber of # as  an area """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end = "")
            print()
