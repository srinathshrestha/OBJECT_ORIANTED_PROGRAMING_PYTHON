class Employee():


    def __init__(self, salary, skill, experiance):  # constructur - saves from the commented code. :)
        self.salary = salary
        self.skill = skill
        self.experiance = experiance


    @ classmethod
    def lis(cls,emp_string):
        salary,skill,experiance = emp_string.split('-')
        return cls(salary,skill,experiance)
    @staticmethod
    def open_or_close(Day): # this dones't auto enters the argument.
        if Day == 'sunady'or'saturday':
            return "Office close"
        elif Day == 'monday'or'tuesday'or'wednesday'or'thrusday'or'friday':
            return 'Office open'

    def __repr__(self):
        return ('Employee salary,skills and expreance is {}, {}, {}').format(self.salary,self.skill,self.experiance)
    def __str__(self):
        return f'skill of the employee is {self.skill}'
    def __add__(self, rohan):
        return self.salary+rohan.salary

if __name__ == '__main__':

    Ayush = Employee.lis('40000-Graphic designer-2 years')
    rohan = Employee(47000, 'front-end development', '4 years')
    srinath = Employee(90000, 'Data Science', '1 year')
    print(srinath.__add__(rohan))
    print(str(srinath))
    print(repr(Ayush)) # visit https://docs.python.org/3/reference/datamodel.html for more dunder methods.