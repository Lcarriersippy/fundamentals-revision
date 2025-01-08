from oop.staff import Staff

class ClassroomStaff(Staff):

    def __init__(self, name, role, languages, working_hours, salary):
        super().__init__(name, role, department='classroom', working_hours = working_hours, salary = salary)
        self.overtime = 0
        self.languages = languages
        self.title = 'junior developer'

    def add_overtime(self, overtime_hours):
        self.overtime += overtime_hours