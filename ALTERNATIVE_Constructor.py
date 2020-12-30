class Employee():
    no_of_employee = 0
    increament = 1.5

    def __init__(self, salary, skill, experiance):  # constructur - saves from the commented code. :)
        self.salary = salary
        self.skill = skill
        self.experiance = experiance
        Employee.no_of_employee = Employee.no_of_employee + 1

    def increase(self):
        self.salary = int(self.salary * (Employee.increament))
    @ classmethod # here we are dealing with obj_attributes
    def lis(cls,emp_string): # we have to creat the classmethod_name as the variable_name{mentioned below}
        salary,skill,experiance = emp_string.split('-')# the arguement_name must be equal to emp_string
        return cls(salary,skill,experiance) # this should return all the attributes of the obj inside the cls.
if __name__ == '__main__':

    Ayush = Employee.lis('40000-Graphic designer-2 years') # cls_name.varibale_name('emp_string') [this will give a list]
    rohan = Employee(47000, 'front-end development', '4 years')
    srinath = Employee(90000, 'Data Science', '1 year')
    print(Ayush.salary)


