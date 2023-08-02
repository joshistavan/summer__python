a=input("please tell about status about Harry Rohan and hamad ")
p=int(input("1 and 2"))
if a=="harry" and p==1:
    x=open("f1.txt",'r')
    o= x.read()
    print(o)
elif a=="harry" and p==2:
    x1=open('f2.txt','r')
    o1=x1.read()
    print(o1)
elif a=="rohan" and p==1:
    s=open("f3.txt",'r')
    s1=s.read()
    print(s1)
elif a=='rohan' and p==2:
    c=open("f4.txt",'r')
    c1=c.read()
    print(c1)
elif a=="hamad " and p==1:
    v=open("f5.txt",'r')
    v1=v.read()
    print(v1)
elif a=='hamad' and p==2:
    k=open('f6.txt',"r")
    k1= k.read()
    print(k1)
# else:
#     print("you dial in valid")