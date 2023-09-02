#!/usr/bin/python3
#!/usr/bin/python3
"""
3-base_geometry module

Define an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    An empty class representing BaseGeometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()
    bg.area()
