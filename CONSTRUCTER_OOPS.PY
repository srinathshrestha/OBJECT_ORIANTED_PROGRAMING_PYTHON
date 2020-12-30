class employee():
    def __init__(self,salary,skill,experiance): #constructur - saves from the commented code. :)
        self.salary=salary
        self.skill=skill
        self.experiance=experiance
if __name__ == '__main__':

    rohan = employee(47000,'front-end development','4 years')
    srinath = employee(90000,'Data Science','1 year')
    # rohan.saraly = 47000
    # srinath.salary = 90000
    # rohan.skill = 'front-end development'
    # srinath.skill ='Data Science'
    # rohan.experiane='3 years'
    # srinath.experiance = '1 year'
    # print(id(srinath))
    # print(type(srinath))
    # print(srinath)
    # print('Rohan\'s skill is' ,rohan.skill,',','Srinath\'s skill is',srinath.skill,',','Rohan\'s salary is',rohan.saraly,',','Srinath\'s salary is',srinath.salary)
    print(f'Rohan\'s skill is {rohan.skill}, srinath\'s skill is {srinath.skill} and their respective salaries are {rohan.salary} and {srinath.salary}')
