class Employee():
    no_of_employee = 0
    increament = 1.5


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

if __name__ == '__main__':

    rohan = Employee(47000,'front-end development','4 years')
    srinath = Employee(90000,'Data Science','1 year')



print(srinath.salary)
srinath.change_increments(2)
srinath.increase()
print(srinath.salary)

