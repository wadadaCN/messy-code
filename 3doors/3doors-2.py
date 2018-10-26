import random
import copy

true = 0
for n in range(10000):
    door = []
    while len(door) < 3:
        r = random.randint(0, 2)
        if r not in door:
            door.append(r)

    goat = door[0]
    choose = door[random.randint(0, 2)]

    temp = copy.deepcopy(door)
    temp.remove(choose)

    excludei = random.randint(0, 1)

    if goat == temp[excludei]:
        door.remove(temp[1 - excludei])
    else:
        door.remove(temp[excludei])
    door.remove(choose)

    choose = door[0]

    if goat == choose:
        true += 1

print(true)
