#!/usr/bin/python3

"""Define class for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
        - data: The data for the node (must be an integer).
        - next_node (Node, optional): The next node in the linked list. Default is None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data attribute.

        Returns:
        - int: The data of the node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data attribute.

        Parameters:
        - value: The new data value.

         Raises:
         - TypeError: if value is not an integer.
         """
         if not isinstance(value, int):
             raise TypeError("data must be an integer")

         self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the data attribute.

        Returns:
        - Node or None: The next node in the linked list.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the next_node attribute.

        Parameters:
        - value: The next node value.

        Raises:
        - TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position in the list (increasing order).

        Parameters:
        - value: The value to be inserted.
        """
        new_node = Node(value)

        if not self.head or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Defines the string representation of the SinglyLinkedList object.

        Returns:
        - str: Astring representation of the linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node

        return ("\n".join(result))
