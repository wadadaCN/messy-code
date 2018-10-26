import random
import copy

true = 0
for n in range(10000):
    check = []
    while len(check) < 4:
        r = random.randint(0, 3)
        if r not in check:
            check.append(r)

    treasure = check[0]
    choose = check[random.randint(0, 3)]

    temp = copy.deepcopy(check)
    temp.remove(choose)

    excludei = random.randint(0, 2)

    if treasure == temp[excludei]:
        check.remove(temp[2 - excludei])
    else:
        check.remove(temp[excludei])
    check.remove(choose)

    choose = check[random.randint(0, 1)]

    if treasure == choose:
        true += 1

print(true)
