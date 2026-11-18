
from models.student import Student
from storage.json_storage import JsonStorage


class StudentService:

    def __init__(self, storage: JsonStorage):
        self.storage = storage
        self.students = self.storage.load_students()

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added.")

        if self.find_student_by_id(student.student_id):
            raise ValueError("A student with this ID already exists.")

        self.students.append(student)
        self.storage.save_students(self.students)

    def get_all_students(self):
        return self.students.copy()

    def find_student_by_id(self, student_id: int):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def update_grade(self, student_id: int, new_grade: str):
        student = self.find_student_by_id(student_id)

        if student is None:
            raise ValueError("Student not found.")

        student.grade = new_grade
        self.storage.save_students(self.students)

    def delete_student(self, student_id: int):
        student = self.find_student_by_id(student_id)

        if student is None:
            raise ValueError("Student not found.")

        self.students.remove(student)
        self.storage.save_students(self.students)

        return student
