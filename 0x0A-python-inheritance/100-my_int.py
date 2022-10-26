#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """rebel version of an interger, perfect for opposite day"""
    def __new__(cls, *args, **kwargs):
        """creating a new instance of a class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne_(self, other):
        """what was == is now !="""
        return int(self) == other
