#!/usr/bin/python3

"""
3-base_geometry module

Define an empty class BaseGeometry.
"""

class BaseGeometry:
    """
    An empty class representing BaseGeometry.
    """

    def __init_subclass__(cls):
        """
        Override the __init_subclass__ method to exclude it from the list of attributes for the class.
        """
        pass

if __name__ == "__main__":
    bg = BaseGeometry()
    print(bg)
    print(dir(bg))

    print(BaseGeometry)
    print(dir(BaseGeometry))
