# ls=[ ]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)


ls=[ i for i in range(100) if i%5==0 ]
print(ls)

dict1={i:f"item{i}" for i in range(100)}
print(dict1)