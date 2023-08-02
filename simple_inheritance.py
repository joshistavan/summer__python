class Employe:

    def __init__(self,asalary,arole,ahoby):
        self.salary=asalary
        self.role=arole
        self.hoby=ahoby

    def emp(self):
        return (self.salary,self.role,self.hoby)

stavan=Employe("salary",'a','a')
Anmol=Employe('salary','a','a')

stavan.salary=123
stavan.role='Developer'
stavan.hoby='coding'

Anmol.salary=321
Anmol.role='python'
Anmol.hoby='Walking'


class programmar(Employe):

    def __init__(self,asalary,arole,ahoby):
        self.salary=asalary
        self.role=arole
        self.hoby=ahoby

ramesh=programmar('salary','role','hoby')


print(ramesh.salary)
p=ramesh.emp()
print(p)

print(Anmol.role)
