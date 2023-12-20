#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The square of the class. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.

        Returns:
        - int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Parameters:
        - value (int): The new size value.

        Raises:
        - TypeError: if value is not an integer.
        - ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return (self.__size ** 2)
