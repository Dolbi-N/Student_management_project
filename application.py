
from storage.json_storage import JsonStorage
from services.student_service import StudentService
from ui.student_controller import StudentController


class Application:

    def __init__(self):
        self.storage = JsonStorage("storage/students.json")
        self.student_service = StudentService(self.storage)
        self.controller = StudentController(self.student_service)

    def run(self):
        self.controller.run()
