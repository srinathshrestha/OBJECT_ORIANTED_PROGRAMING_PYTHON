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
if __name__ == '__main__':

    print(Employee.no_of_employee)
    rohan = Employee(47000,'front-end development','4 years')
    print(Employee.no_of_employee)
    srinath = Employee(90000,'Data Science','1 year')
    print(Employee.no_of_employee)
    # print(srinath.__dict__) # gives the attributes of the obj
    # print(employee.__dict__)
    print(srinath.salary)
    srinath.increase()
    print(srinath.salary)