import random

pl_pos = 1
com_pos = 1

def banmen():
    print("・"*(pl_pos-1) + "P" + "・"*(30-pl_pos)+"Goal")
    print("・"*(com_pos-1) + "C" + "・"*(30-com_pos)+"Goal")


print("start sugoroku")
while True:

    banmen()
    input("If you put Enter, your piece is moved.")

    pl_pos = pl_pos + random.randint(1,6)

    if pl_pos>=30:
        pl_pos=30

    banmen()

    if pl_pos==30:
        print("you win")
        break

    input("If you put Enter, CPU piece is moved.")

    com_pos = com_pos + random.randint(1,6)

    if com_pos>=30:
        com_pos=30

    banmen()

    if com_pos==30:
        print("you lose")
        break
