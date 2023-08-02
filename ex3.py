inp=input("Please Enter True or False ")
if inp=="true":
    a=int(input('enter your choice'))
    for i in range(a):
        print(i*"*")
else:
    x=int(input('enter your choice'))
    for i in range(x,0,-1):
        print(i*"*")