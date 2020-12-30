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
if __name__ == '__main__':

    Ayush = Employee.lis('40000-Graphic designer-2 years')
    rohan = Employee(47000, 'front-end development', '4 years')
    srinath = Employee(90000, 'Data Science', '1 year')
    print(srinath.open_or_close("saturday"))


