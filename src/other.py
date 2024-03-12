"""
Sample class.    
"""


class Person:
    """
    Basic class to represent a person.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> None:
        """
        Greets the person.
        """

        print(f"Hello, {self.name}. I can't believe you're {self.age} years old!")

    def have_birthday(self) -> None:
        """
        Age one year.
        """

        self.age += 1
