l=10   # global
def fun1(n):
    # l=5
    m=1   #local
    global l
    l+=10
    print(l)
    print(n,"hello")
fun1("world")
print(l)
