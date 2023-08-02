# class Emp:
#     def printdetail(self):
#         return [self.name,self.salary,self.role]
# stavan=Emp()
# anmol=Emp()
# stavan.name="stavan Kumar"
# stavan.salary=100000
# stavan.role='python developer'
# anmol.name='Anmol kumar'
# anmol.salary='12000'
# anmol.role='student'
#
# x=(anmol.printdetail())
# print(x)
#---------------------------------------------------------------------------~~
#class emp:
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#
# stavan=emp('name','salary','role')
# stavan.name='Stavan kumar'
# stavan.salary=10000
# stavan.role='Python Developer'
#
# print(stavan.salary)
#---------------------------------------------------------------------
# class Emp:
#     def __init__(self,aname,arole,aid):
#         self.name='aname'
#         self.role='arole'
#         self.id='aid'
#
#
# anmol=Emp('name','role','id')
#
# anmol.name='Anmol Kumar'
# anmol.role='Student'
# anmol.id=11
#
# print(anmol.id)
#----------------------------------------------------------------

# class Employe:
#     no_of_leave=9
#     def __init__(self,aname,asalary,aid):
#         self.name=aname
#         self.salary=asalary
#         self.id=aid
#     @classmethod
#     def change_leavs(cls,newleavs):
#         cls.no_of_leave=newleavs
# stavan=Employe("stavan",123,1)
# stavan.change_leavs(22)
#
# name='stavan'
# salary=123
# id=1
# print(stavan.no_of_leave)

#---------------------------------------------------------------
class Employe:

    def __init__(self,asalary,arole,ahoby):
        self.salary=asalary
        self.role=arole
        self.hoby=ahoby

    # def emp(self):
    #     return (self.salary,self.role,self.hoby)

stavan=Employe("salary",'a','a')
Anmol=Employe('salary','a','a')

stavan.salary=123
stavan.role='Developer'
stavan.hoby='coding'

Anmol.salary=321
Anmol.role='python'
Anmol.hoby='Walking'

print(Anmol.role)

# class programmar(Employe):
#     pass
#
#     def __init__(self,asalary,arole,ahoby):
#         self.salary=asalary
#         self.role=arole
#         self.hoby=ahoby
#
# ramesh=programmar('salary','role','hoby')
#
#
# print(ramesh.salary)
















































