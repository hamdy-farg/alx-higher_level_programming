#!/usr/bin/python3
""" dasgdasg """
class Square:
    """ dasgf"""
    def __init__(self, size = 0):
        """ dsag"""
        self.__size = size

        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError ("size must be >= 0")
