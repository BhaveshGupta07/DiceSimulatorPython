import random

def diceroll():

    a="y"
    while a =="y":
        x=random.randint(1,6)
        if x==1:
            print("------------------------------")
            print("|                             |")
            print("|              0              |")
            print("|                             |")
            print("------------------------------")
        if x==2:
            print("------------------------------")
            print("|                             |")
            print("|          0       0          |")
            print("|                             |")
            print("------------------------------")
        if x==3:
            print("------------------------------")
            print("|              0             |")
            print("|          0        0         |")
            print("|                             |")
            print("------------------------------")
        if x==4:
            print("------------------------------")
            print("|         0         0         |")
            print("|                             |")
            print("|         0         0         |")
            print("------------------------------")
        if x==5:
            print("------------------------------")
            print("|         0         0         |")
            print("|              0              |")
            print("|         0         0         |")
            print("------------------------------")
        if x==6:
            print("------------------------------")
            print("|         0         0         |")
            print("|         0         0         |")
            print("|         0         0         |")
            print("------------------------------")
       
        a=input("do you want to continue press y or n ?")

diceroll()