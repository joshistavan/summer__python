#this is filter Function.

lst=[1,2,3,4,5,6,7,8,9]
def gr(num):
    return num>5
g = list(filter(gr,lst))
print(g)