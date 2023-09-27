#!/usr/bin/python3
""" dasgdasg  adsf"""
class Square:
    """ dasg fsdaff"""
    def __init__ (self, size = 0):
        """ fasf dsag"""
        self.__size = size

        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
