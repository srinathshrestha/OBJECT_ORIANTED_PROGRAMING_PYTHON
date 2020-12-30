class Employee():
    no_of_employee = 0
    increament = 2.5


    def __init__(self,salary,skill,experiance): #constructur - saves from the commented code. :)
        self.salary=salary
        self.skill=skill
        self.experiance=experiance
        Employee.no_of_employee = Employee.no_of_employee+1


    def increase(self):
        self.salary = int(self.salary * (Employee.increament))

    @classmethod # here we are dealing with cls_variables

    def change_increments(cls,amout):
        Employee.increament = amout

rohan = Employee(47000,'front-end development','4 years')
srinath = Employee(90000,'Data Science','1 year')


class Coder(Employee):
    def __init__(self,salary,skill,experiance,programing_language):
        super().__init__(salary,skill,experiance) # we dont't require self here
        self.programing_language = programing_language

    def increase(self):
        self.salary = int(self.salary * (Employee.increament + 2.2))


samul_miller = Coder(60000,'coding','10 years','java')
samul_miller.increase()
        # print(samul_miller.salary)

# special code ;D
help(Coder)