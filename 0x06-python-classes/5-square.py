#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def _init_(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
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
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square with the # character.
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range (self.__size)]
            print("")
        if self.__size == 0:
            print("")
