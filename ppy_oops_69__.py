class Employee:
    def __init__(self,fname,lname,):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f" This Employee is {self.fname} {self.lname}"
    @property   # it is use we can not use ().
    def email(self):
        return f" {self.fname} {self.lname}@gmail.com"

hindustan_supporter=Employee('hindustani','supporter')
stavan_joshi=Employee("Stavan","joshi")
print(stavan_joshi.email)

hindustan_supporter.fname="us"

print(hindustan_supporter.email)
