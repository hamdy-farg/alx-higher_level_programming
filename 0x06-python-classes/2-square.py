#!/usr/bin/python3
class Square:
    """ dasgf"""
    def __init__(self, size = 0):
        """ adsgg """
        self.__size = size
        try:
            if type(self.__size) != int:
                raise TypeError("size must be an integer")
            elif self.__size < 0:
                raise ValueError ("size must be >= 0")
        except ValueError or TypeError: 
            raise
