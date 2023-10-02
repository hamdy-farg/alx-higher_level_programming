#!/usr/bin/python3
''' class recgsadg '''
class Rectangle:
    ''' impelemnt it'''
    def __init__ (self, width = 0, height = 0):
        ''' init some values '''
        self.__rectangle__height = height
        self.__rectangle__width = width

        
    @property
    def width(self):
        ''' return width '''
        return self.__rectangle__width
        
    @property
    def height(self):
        ''' height return '''
        return self.__rectangle__height
    
    @width.setter
    def width(self, value):
        ''' width return '''
        if(type(value) != int):
            raise TypeError ("width must be an integer")
        if(value  < 0):
            raise ValueError ("width must be >= 0")
        self.__rectangle__width = value

    @height.setter
    def height(self, value):
        ''' height set '''
        if(type(value) != int):
            raise TypeError ("height must be an integer")
        if(value < 0):
            raise ValueError ("hight must be >= 0")
        self.__rectangle__height = value
        

