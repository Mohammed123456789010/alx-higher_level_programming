#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width the new rectangle.
            heigth (int): The height of the new rectangle.
        """
        self.width = width
        self.heigth = height

@property
def width(self):
    """Get/set the width of the Rectangle."""
    return self.__width

@width.setter
def width(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("heigth must be >= 0")
    self.__heigth = value

def area(self):
    """Return the primeter of the Rectangle."""
    if self.__width == 0 or self.__height == 0:
        return (0)
    return ((self.__width * 2) + (self.__height * 2))
