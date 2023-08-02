# i=1
# while (1):
#     print(i)
#     if i==40:
#         break
#     i+=1
# while True:
#         num=int(input('guess the number'))
#         if num>100:
#             print('ok')
#             break
# a = 18
# gus = 1
# while gus <= 9:
#     num = int(input('entetr the number'))
#     if num < 18:
#         print('please incress the number')
#     elif num > 18:
#         print('please decress the number')
#     else:
#         print('congrulation you are win')
#         print(gus, 'bhai you have ')
#         break
#      print(9 - gus, 'you have left')
#                         gus += 1
#                         if gus < 9:
#                             print('game over')
# n=18
# gus = 1
# while gus<=9:
#     a = int(input("enter any number"))
#     if a>18:
#         print("decress the number")
#     elif a<18:
#         print("incres the number")
#     else:
#         print('congo you can win')
#         print(gus,'you have left gus')
#         break
#     print(9-gus,'you have gus')
#     gus+=1
#     if gus<9:
#         print('game is over')

n=18
gus=1
while gus<=9:
    a = int(input('enter your choice number'))
    if n>a:
        print('incress your choice')
    elif n<a:
        print('decress your choice')
    else:
        print('congo')
        print(gus,'you have already gus')
        break
    print(9-gus,'your gus')
    gus+=1
    if gus<9:
        print('the game is over')



















