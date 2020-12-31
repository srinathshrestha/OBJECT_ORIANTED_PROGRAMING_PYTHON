class Emp():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name= last_name
    @property
    def email(self):
        if self.first_name == None:
            return "Email is not set"
        else:
            mail = self.first_name+'.'+self.last_name+'@email.com'
            return mail
    @email.setter
    def email(self,given_emial):
        lis = given_emial.split('@')[0].split('.')
        self.first_name = lis[0]
        self.last_name = lis[1]
    @email.deleter
    def email(self):
        self.first_name = None
        self.last_name = None

srinath= Emp('srinath','shrestha')
ayush= Emp('Ayush','mehra')
print(srinath.email)
srinath.email='shrestha.srinath@email.com'
print(srinath.email)
del srinath.email
print(srinath.email)













