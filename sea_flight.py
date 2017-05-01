# -*-coding:utf8;-*-
# qpy:3
# qpy:console
import random

SIZE = 10


def is_ship(sea, x, y):
    if sea[x][y] == 1:
        return True
    else:
        return False


def is_free4(sea, x, y, direct):
    if direct == 1:
        if x + 3 < SIZE:
            return True
        else:
            return False
    else:
        if y + 3 < SIZE:
            return True
        else:
            return False


def is_busy(sea, x, y):
    return is_ship(sea, x, y) or (sea[x][y] == 2)


def is_free3(sea, x, y, direct):
    if direct == 1:
        if x + 2 < SIZE:
            if (not is_busy(sea, x, y)) and (not is_busy(sea, x + 1, y)) and (not is_busy(sea, x + 2, y)):
                return True
            else:
                return False
        else:
            return False
    else:
        if y + 2 < SIZE:
            if (not is_busy(sea, x, y)) and (not is_busy(sea, x, y + 1)) and (not is_busy(sea, x, y + 2)):
                return True
            else:
                return False
        else:
            return False


def is_free2(sea, x, y, direct):
    if direct == 1:
        if x + 1 < SIZE:
            if (not is_busy(sea, x, y)) and (not is_busy(sea, x + 1, y)):
                return True
            else:
                return False
        else:
            return False
    else:
        if y + 1 < SIZE:
            if (not is_busy(sea, x, y)) and (not is_busy(sea, x, y + 1)):
                return True
            else:
                return False
        else:
            return False


def is_free1(sea, x, y):
    return not is_busy(sea, x, y)


def sea_neibor(sea, x, y):
    if (x >= 0) and (x < SIZE) and (y >= 0) and (y < SIZE):
        if sea[x][y] != 1:
            sea[x][y] = 2


def set_ship(sea, x, y):
    sea[x][y] = 1
    sea_neibor(sea, x - 1, y)
    sea_neibor(sea, x, y - 1)
    sea_neibor(sea, x + 1, y)
    sea_neibor(sea, x, y + 1)
    sea_neibor(sea, x - 1, y - 1)
    sea_neibor(sea, x + 1, y + 1)
    sea_neibor(sea, x - 1, y + 1)
    sea_neibor(sea, x + 1, y - 1)


def ship4():
    x = random.randint(0, SIZE - 1)
    y = random.randint(0, SIZE - 1)
    direct = random.randint(0, 1)

    while not is_free4(sea, x, y, direct):
        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)
        direct = random.randint(0, 1)  # 0 Вертикаль 1 горизонтально

    if direct == 1:
        set_ship(sea, x, y)
        set_ship(sea, x + 1, y)
        set_ship(sea, x + 2, y)
        set_ship(sea, x + 3, y)
    else:
        set_ship(sea, x, y)
        set_ship(sea, x, y + 1)
        set_ship(sea, x, y + 2)
        set_ship(sea, x, y + 3)


def ship3():
    x = random.randint(0, SIZE - 1)
    y = random.randint(0, SIZE - 1)
    direct = random.randint(0, 1)  # 0 Вертикаль 1 горизонтально

    while not is_free3(sea, x, y, direct):
        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)
        direct = random.randint(0, 1)
    if direct == 1:
        set_ship(sea, x, y)
        set_ship(sea, x + 1, y)
        set_ship(sea, x + 2, y)
    else:
        set_ship(sea, x, y)
        set_ship(sea, x, y + 1)
        set_ship(sea, x, y + 2)


def ship2():
    x = random.randint(0, SIZE - 1)
    y = random.randint(0, SIZE - 1)
    direct = random.randint(0, 1)  # 0 Вертикаль 1 горизонтально

    while not is_free2(sea, x, y, direct):
        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)
        direct = random.randint(0, 1)
    if direct == 1:
        set_ship(sea, x, y)
        set_ship(sea, x + 1, y)
    else:
        set_ship(sea, x, y)
        set_ship(sea, x, y + 1)


def ship1():
    x = random.randint(0, SIZE - 1)
    y = random.randint(0, SIZE - 1)

    while not is_free1(sea, x, y):
        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)

    set_ship(sea, x, y)


def count_not_free(sea):
    k = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if sea[i][j] == 1:
                k = k + 1
    return k


def print_sea(sea):
    print("    ", end="")
    for j in range(10):
        print(j, end="  ")
    print()
    print("  +-----------------------------")
    for i in range(SIZE):
        print(i, end=" | ")
        for j in range(SIZE):
            if sea[i][j] < 0:
                print(sea[i][j], end=" ")
            else:
                print(sea[i][j], end="  ")

        print()


sea = [[0 for i in range(SIZE)] for j in range(SIZE)]

random.seed()

ship4()
ship3()
ship3()
ship2()
ship2()
ship2()
ship1()
ship1()
ship1()
ship1()

sea_map = [[0 for i in range(SIZE)] for j in range(SIZE)]

for i in range(SIZE):
    for j in range(SIZE):
        if sea[i][j] == 2:
            sea[i][j] = 0

while True:
    o = count_not_free(sea)
    print("Залишилось", o, "палуб")
    x = int(input("Введіть вертикаль"))
    y = int(input("Введіть горизонталь"))

    if is_ship(sea, x, y):
        print("Попав!")
        sea_map[x][y] = 2
        sea[x][y] = 0
    else:
        print("Мимо")
        sea_map[x][y] = -1

    print_sea(sea_map)