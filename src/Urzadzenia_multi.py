import random
import numpy
import matplotlib.pyplot as plt

'''
a => moment włączenia urządzenia
b => lista poboru energii
c => czas dostarczania energii elektrycznej
d => odstęp pomiędzy poborami energii w ramach jednego użycia
e => odstęp czasowy pomiędzy użyciami
'''


def zelazko(a, c, d, e):
    b = []
    liczba_uzyc = random.randint(1, 20)
    for i in range(0, round(a)):
        b.append(0)
    for i in range(0, liczba_uzyc):
        if i == 0:
            temp = random.randrange(45, 55)
            for j in range(0, round(temp)):
                b.append(2400)
        for j in range(0, round(c)):
            b.append(2400)
        for j in range(0, round(d)):
            b.append(15)
    for i in range(0, round(e)):
        b.append(0)
    # czas = numpy.linspace(0, len(b), len(b))
    # plt.plot(czas, b)
    # plt.xlabel('Czas [s]')
    # plt.ylabel('Moc [W]')
    # plt.title('Żelazko')
    # plt.show()
    return b

def telewizor(a, c, e):
    b = []
    for i in range(0, round(a)):
        b.append(26)
    for i in range(0, round(c)):
        b.append(70)
    for i in range(0, round(e)):
        b.append(26)
    # czas = numpy.linspace(0, len(b), len(b))
    # plt.plot(czas, b)
    # plt.xlabel('Czas [s]')
    # plt.ylabel('Moc [W]')
    # plt.title('Telewizor')
    # plt.show()
    return b

def odkurzacz(a, c, d, e):
    b = []
    liczba_uzyc = random.randint(1, 3)
    for i in range(0, round(a)):
        b.append(0)
    for i in range(0, liczba_uzyc):
        for k in range(0, round(c)):
            b.append(600)
        for k in range(0, round(d)):
            b.append(0)
    for k in range(0, round(e)):
        b.append(0)
    # czas = numpy.linspace(0, len(b), len(b))
    # plt.plot(czas, b)
    # plt.xlabel('Czas [s]')
    # plt.ylabel('Moc [W]')
    # plt.title('Odkurzacz')
    # plt.show()
    return b

def oswietlenie(a, c, e):
    b = []
    for i in range(0, round(a)):
        b.append(0)
    for i in range(0, round(c)):
        b.append(8)
    for j in range(0, round(e)):
        b.append(0)
    # czas = numpy.linspace(0, len(b), len(b))
    # plt.plot(czas, b)
    # plt.xlabel('Czas [s]')
    # plt.ylabel('Moc [W]')
    # plt.title('Oswietlenie')
    # plt.show()
    return b

def lodowka(a, c, d, e):
    b = []
    liczba_wlaczen = random.randint(3, 10)
    for i in range(0, round(a)):
        b.append(0)
    for i in range(0, liczba_wlaczen):
        for j in range(0, round(c)):
            b.append(131)
        for j in range(0, round(d)):
            b.append(11)
    for i in range(0, round(e)):
        b.append(0)
    # czas = numpy.linspace(0, len(b), len(b))
    # plt.plot(czas, b)
    # plt.xlabel('Czas [s]')
    # plt.ylabel('Moc [W]')
    # plt.title('Lodowka')
    # plt.show()
    return b

def pralka(a, e):
    b = []
    tryb = random.randint(1, 2)
    if tryb == 1:
        for j in range(0, 120):
            b.append(40)
        for j in range(0, 120):
            b.append(1660)
        for j in range(0, 900):
            b.append(300)
        for j in range(0, 240):
            b.append(2000)
        for j in range(0, 240):
            b.append(40)
        for j in range(0, 120):
            b.append(1660)
        for j in range(0, 900):
            b.append(300)
        for j in range(0, 360):
            b.append(40)
        for j in range(0, 600):
            b.append(300)
        for j in range(0, round(e)):
            b.append(0)
    else:
        for j in range(0, 120):
            b.append(40)
        for j in range(0, 180):
            b.append(1660)
        for j in range(0, 480):
            b.append(300)
        for j in range(0, 600):
            b.append(2000)
        for j in range(0, 480):
            b.append(300)
        for j in range(0, 60):
            b.append(40)
        for j in range(0, 600):
            b.append(2000)
        for j in range(0, 900):
            b.append(300)
        for j in range(0, 180):
            b.append(40)
        for j in range(0, 600):
            b.append(300)
        for j in range(0, round(e)):
            b.append(0)
    # czas = numpy.linspace(0, len(b), len(b))
    # plt.plot(czas, b)
    # plt.xlabel('Czas [s]')
    # plt.ylabel('Moc [W]')
    # plt.title('Pralka')
    # plt.show()
    return b
