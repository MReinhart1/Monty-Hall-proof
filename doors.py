import random
def dontswitch():
    doors = [0,0,0]
    newCar = random.randint(0,2)
    doors[newCar] = 1
    choose = random.randint(0,2)
    if doors[0] != 1 and choose != 0:
        openedDoor = 0
    elif doors[1] != 1 and choose != 1:
        openedDoor = 1
    else:
        openedDoor = 2
    if doors[choose] == 1:
        return 1
    else:
        return 0


def doswitch():
    doors = [0,0,0]
    newCar = random.randint(0,2)
    doors[newCar] = 1
    choose = random.randint(0,2)
    if doors[0] != 1 and choose != 0:
        openedDoor = 0
    elif doors[1] != 1 and choose != 1:
        openedDoor = 1
    else:
        openedDoor = 2
    doors[openedDoor] = 77
    doors[choose] = 77
    doors.remove(77)
    doors.remove(77)
    if doors[0] == 1:
        return 1
    else:
        return 0

winsDont = 0
winsDo = 0
for i in range(0,10000000):
    if dontswitch() == 1:
        winsDont+= 1
    if doswitch() == 1:
        winsDo+= 1
print(winsDont, winsDo)
