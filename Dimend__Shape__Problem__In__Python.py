class A:
    def met(self):
        print("This is from Class A")

class B(A):
    def met(self):
        print("This is from Class B")

class C(A):
    def met(self):
        print("This is from Class C")

class D(B,C):
    def met(self):
        print("This is from Class D")

a=A()
b=B()
c=C()
d=D()

d.met()
