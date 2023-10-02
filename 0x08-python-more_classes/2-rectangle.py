''' this Rectangle class '''
class Rectangle:
    ''' implementation for this '''
    def __init__ (self, width = 0, height = 0):
        ''' assignment opertator for values '''
        self.__rectangle__height = height 
        self.__rectangle__width = width

        
    @property
    def width(self):
        ''' let me know width '''
        return self.__rectangle__width
        
    @property
    def height(self):
        ''' let me know the hight '''
        return self.__rectangle__height
    
    @width.setter
    def width(self, value):
        ''' set the width for me '''
        if(type(value) != int):
            raise TypeError ("width must be an integer")
        if(value  < 0):
            raise ValueError ("width must be >= 0")
        self.__rectangle__width = value

    @height.setter
    def height(self, value):
        ''' set the height for me '''
        if(type(value) != int):
            raise TypeError ("height must be an integer")
        if(value < 0):
            raise ValueError ("height must be >= 0")
        self.__rectangle__height = value
        
    def area(self):
        ''' return area '''
        return (self.__rectangle__height * self.__rectangle__width)
        
    def perimeter(self):
        ''' return perimeter '''
        if (self.__rectangle__width == 0 or self.__rectangle__height == 0):
            return 0
        return (self.__rectangle__width + self.__rectangle__height ) * 2
