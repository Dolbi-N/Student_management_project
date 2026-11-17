
from models.person import Person


class Student(Person):

    VALID_GRADES = ("A", "B", "C", "D", "E", "F")

    def __init__(self, name: str, student_id: int, grade: str):
        super().__init__(name)
        self.student_id = student_id
        self.grade = grade

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value: int):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Student ID must be an integer.")

        if value <= 0:
            raise ValueError("Student ID must be positive.")

        self.__student_id = value

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Grade must be a string.")

        value = value.strip().upper()

        if value not in self.VALID_GRADES:
            raise ValueError("Grade must be between A and F.")

        self.__grade = value

    def get_details(self):
        return (
            f"Name: {self.name}, "
            f"Student ID: {self.student_id}, "
            f"Grade: {self.grade}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grade": self.grade
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            student_id=data["student_id"],
            grade=data["grade"]
        )
