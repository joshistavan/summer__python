class student:
    pass
stavan=student()
anmol=student()

stavan.salary=123
stavan.std=11
stavan.sub='python'

anmol.salary=12
anmol.std=10
anmol.sub='python Developer'

print(stavan.__dict__)
print(anmol.salary)