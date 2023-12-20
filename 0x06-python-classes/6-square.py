#!/usr/bin/python3
"""sqare module"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """constractor.

        args:
                        size: size of the square
        raisees:
            typeerror: type of the square
            valueerror: value of the square
        """

        self.size = size

    @property
    def size(self):
        """property for size of the square

        raises:
            typeerror: type of the square
            valueerror: value of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area of the object

        returns:
            the size of the object
        """
        return self.__size**2

    def my_print(self):
        """print the object"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
