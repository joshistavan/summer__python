class A:
    dance=9
    name="anmoljoshi"

    def myname(self):
        return f"My name is Anmol JOhsi{self.name}"
class B:
    dance=7
    name='stavanjoshsi'
    def myname(self):
        return f"My name is Stavan JOhsi{self.name}"
class C(A,B):
    garba=1
    pass

stavan=A()
anmol=B()
chetan=C()

print(chetan.myname())