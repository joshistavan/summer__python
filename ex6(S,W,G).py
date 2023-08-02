import random
list=["s","w","g"]
ls=random.choice(list)
print(ls)
you=0
com=0
chance=1
while (True):
    inp=input('Enter your choice S W G')
    if inp=="s" and ls=="w":
        print("you win")
        you+=1
    elif inp=="w" and ls=="g":
        print("you win")
        you+=1
    elif inp=="g" and ls=="s":
        print("you win")
        you+=1
    elif you==com:
        print("this match will be tai")
    else:
        print("com win")
        chance+=1
        if chance>=5:
            break

