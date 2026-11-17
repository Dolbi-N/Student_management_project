
class Person:

    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")

        if not value.strip():
            raise ValueError("Name cannot be empty.")

        self.__name = value.strip()

    def get_details(self):
        return f"Name: {self.name}"
