from enum import Enum


class Person:
    def __init__(self, name):
        self.name = name


class Relationship(Enum): # <-- Happy family of 6.
    PARENT = 1
    CHILD = 2
    SIBLING = 3