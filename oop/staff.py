class Staff():
    def __init__(self, name, role, department, working_hours = 34, salary = 26000):
        self.name = name
        self.role = role
        self.department = department
        self.employed_at_NC = True
        self.working_hours = working_hours
        self.salary = salary


    def update_working_hours(self, new_hours):
        self.working_hours = new_hours

    def increase_salary(self, addition_to_salary):
            self.salary += addition_to_salary

    def fire(self, hr_report):
        if(hr_report['approved']):
            self.employed_at_NC = False
