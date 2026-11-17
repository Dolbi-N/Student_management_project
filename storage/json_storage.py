
import json

from models.student import Student


class JsonStorage:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_students(self, students: list[Student]):
        data = [student.to_dict() for student in students]

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

        except OSError as error:
            raise OSError(f"Could not save students: {error}") from error

    def load_students(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("JSON file must contain a list.")

            return [Student.from_dict(item) for item in data]

        except FileNotFoundError:
            return []

        except json.JSONDecodeError as error:
            raise ValueError("JSON file contains invalid data.") from error

        except OSError as error:
            raise OSError(f"Could not load students: {error}") from error
