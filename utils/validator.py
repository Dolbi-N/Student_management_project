
class Validator:

    @staticmethod
    def validate_name(name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        name = name.strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        if not all(
            char.isalpha() or char.isspace() or char == "-"
            for char in name
        ):
            raise ValueError("Name must contain only letters, spaces or hyphens.")

        return name.title()

    @staticmethod
    def validate_student_id(student_id: str):
        if not student_id.isdigit():
            raise ValueError("Student ID must contain only digits.")

        student_id = int(student_id)

        if student_id <= 0:
            raise ValueError("Student ID must be positive.")

        return student_id

    @staticmethod
    def validate_grade(grade: str):
        if not isinstance(grade, str):
            raise TypeError("Grade must be a string.")

        grade = grade.strip().upper()

        if grade not in ("A", "B", "C", "D", "E", "F"):
            raise ValueError("Grade must be between A and F.")

        return grade
