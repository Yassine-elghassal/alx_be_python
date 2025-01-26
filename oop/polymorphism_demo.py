# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method that raises an error indicating it needs to be overridden."""
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Constructor to initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Constructor to initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
