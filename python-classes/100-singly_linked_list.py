#!/usr/bin/python3
"""Module that defines a Node and SinglyLinkedList class"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node

        Args:
            data: The data to store in the node
            next_node: The next node in the list (default: None)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data for the node

        Args:
            value: The data value to set

        Raises:
            TypeError: If data is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node

        Args:
            value: The next node (must be None or a Node object)

        Raises:
            TypeError: If next_node is not None or a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize an empty singly linked list"""
        self.__head = None

    def __str__(self):
        """String representation of the list"""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position

        Args:
            value: The value to insert (in increasing order)
        """
        new_node = Node(value)

        # If list is empty or new value is smaller than head
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Find the correct position to insert
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        # Insert the new node
        new_node.next_node = current.next_node
        current.next_node = new_node
