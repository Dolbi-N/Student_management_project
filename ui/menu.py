
class Menu:

    @staticmethod
    def display_menu():
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. List all students")
        print("3. Search student by ID")
        print("4. Update student grade")
        print("5. Exit")

    @staticmethod
    def get_choice():
        return input("Enter your choice (1-5): ")
