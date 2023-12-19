#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """
        Initializes a new instances of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
