#!/usr/bin/python3
""" bla vla bla """

class Square:
    """ square class """
    def __init__(self, size=0, position= (0, 0)):
        """ small intialization """
        if  (len(position) != 2):
            raise TypeError ("position must be a tuple of 2 positive integers")
        self.__position = position
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
        for i in range(self.__position[1]):
            print()
            
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print("_", end="")
            for j in range(self.__size):
                print("#", end = "")
            print()
    @property
    def position(self):
        """ positoin getter funciton """
        return self.__position
    
    @position.setter
    def position(self, value):
        """ position func """
        if  (len(value) != 2) :
            raise TypeError ("position must be a tuple of 2 positive integers")
        self.__position = position
