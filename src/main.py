"""
General testing.
"""

from other import Person


def main() -> None:
    """
    Entrypoint.
    """

    print("Hello, world!")

    me: Person = Person("John", 37)
    me.greet()
    me.have_birthday()
    me.greet()
    me.have_birthday()


if __name__ == "__main__":
    main()
