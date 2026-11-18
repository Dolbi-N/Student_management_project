
from models.student import Student
from services.student_service import StudentService
from utils.validator import Validator
from ui.menu import Menu


class StudentController:

    MAX_ATTEMPTS = 5

    def __init__(self, student_service: StudentService):
        self.student_service = student_service

    def get_valid_input(self, prompt, validator):
        for attempt in range(self.MAX_ATTEMPTS):
            user_input = input(f"{prompt}: ").strip()

            if user_input == "0":
                print("\nReturning to main menu...")
                return None

            try:
                return validator(user_input)

            except (ValueError, TypeError) as error:
                remaining_attempts = self.MAX_ATTEMPTS - attempt - 1

                if remaining_attempts > 0:
                    print(
                        f"Error: {error}. "
                        f"Attempts remaining: {remaining_attempts}"
                    )
                else:
                    print("Maximum attempts reached.")

        return None

    def validate_unique_student_id(self, value):
        student_id = Validator.validate_student_id(value)

        if self.student_service.find_student_by_id(student_id) is not None:
            raise ValueError("A student with this ID already exists.")

        return student_id

    def validate_existing_student_id(self, value):
        student_id = Validator.validate_student_id(value)

        if self.student_service.find_student_by_id(student_id) is None:
            raise ValueError("Student not found. Please enter an existing ID.")

        return student_id

    def validate_delete_confirmation(self, value):
        value = value.lower()

        if value not in ("y", "yes", "n", "no"):
            raise ValueError("Please enter y or n.")

        return value

    def add_student(self):
        print("\n===== ADD NEW STUDENT =====")
        print("(Enter 0 at any step to return to main menu)")

        name = self.get_valid_input(
            "Enter student name",
            Validator.validate_name
        )

        if name is None:
            return

        student_id = self.get_valid_input(
            "Enter student ID",
            self.validate_unique_student_id
        )

        if student_id is None:
            return

        grade = self.get_valid_input(
            "Enter student grade",
            Validator.validate_grade
        )

        if grade is None:
            return

        try:
            student = Student(name, student_id, grade)
            self.student_service.add_student(student)

            print("\nStudent added successfully.")

        except (ValueError, TypeError) as error:
            print(f"\nError: {error}")

    def list_students(self):
        students = self.student_service.get_all_students()

        if not students:
            print("\nNo students found.")
            return

        print("\n===== STUDENT LIST =====")

        for student in students:
            print(student.get_details())

    def search_student(self):
        print("\n===== SEARCH STUDENT =====")
        print("(Enter 0 to return to main menu)")

        student_id = self.get_valid_input(
            "Enter student ID",
            Validator.validate_student_id
        )

        if student_id is None:
            return

        student = self.student_service.find_student_by_id(student_id)

        if student is None:
            print("\nStudent not found.")
            return

        print("\n===== STUDENT DETAILS =====")
        print(student.get_details())

    def update_student_grade(self):
        print("\n===== UPDATE STUDENT GRADE =====")
        print("(Enter 0 at any step to return to main menu)")

        student_id = self.get_valid_input(
            "Enter student ID",
            self.validate_existing_student_id
        )

        if student_id is None:
            return

        new_grade = self.get_valid_input(
            "Enter new grade",
            Validator.validate_grade
        )

        if new_grade is None:
            return

        try:
            self.student_service.update_grade(student_id, new_grade)
            print("\nStudent grade updated successfully.")

        except (ValueError, TypeError) as error:
            print(f"\nError: {error}")

    def delete_student(self):
        print("\n===== DELETE STUDENT =====")
        print("(Enter 0 at any step to return to main menu)")

        student_id = self.get_valid_input(
            "Enter student ID",
            self.validate_existing_student_id
        )

        if student_id is None:
            return

        student = self.student_service.find_student_by_id(student_id)

        print("\nStudent to be deleted:")
        print(student.get_details())

        confirmation = self.get_valid_input(
            "Are you sure you want to delete this student? (y/n)",
            self.validate_delete_confirmation
        )

        if confirmation is None:
            return

        if confirmation in ("n", "no"):
            print("\nDeletion cancelled.")
            return

        try:
            deleted_student = self.student_service.delete_student(student_id)
            print(
                f"\nStudent {deleted_student.name} "
                "deleted successfully."
            )

        except (ValueError, TypeError) as error:
            print(f"\nError: {error}")

    def run(self):
        while True:
            Menu.display_menu()
            choice = Menu.get_choice()

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.list_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student_grade()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("\nExiting Student Management System.")
                break

            else:
                print("\nInvalid choice. Please select a number from 1 to 6.")
