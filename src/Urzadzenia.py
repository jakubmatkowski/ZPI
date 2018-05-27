import random
import numpy
import matplotlib.pyplot as plt

'''
a => długość działania urządzenia w ramach jednego użycia
b => czas, w którym urządzenia jest włączone, pobiera energię
c => pobór mocy, on/off
d => odstęp pomiędzy poborami energii w ramach jednego użycia
e => odstęp czasowy pomiędzy użyciami
b_zelazka = random.gauss(7.85, 1.21)
c_zelazka = 2400
d_zelazka = random.expovariate(0.1) + 50
e_zelazka = random.randint(30*60, 30*3600)
'''

class Urzadzenia:

    def zelazko(self):
        dane_zelazko_wl = []
        dane_zelazko_b = []
        dane_zelazko_c = []
        dane_zelazko_d = []
        liczba_uzyc = random.randint(1, 5)
        liczba_wlaczen = random.randint(1, 20)
        for i in range(0, liczba_uzyc):
            tryb = random.randint(1, 3)
            if tryb == 1:
                for j in range(0, liczba_wlaczen):
                    if j == 0:
                        temp = random.randrange(45, 55)
                        dane_zelazko_wl.append(temp)
                        for k in range(0, round(temp)):
                            dane_zelazko_c.append(2400)
                    temp = random.gauss(7.85, 1.5)
                    dane_zelazko_b.append(temp)
                    for k in range(0, round(temp)):
                        dane_zelazko_c.append(2400)
                    temp = random.expovariate(0.05)
                    dane_zelazko_d.append(temp)
                    for k in range(0, round(temp)):
                        dane_zelazko_c.append(15)
                dane_zelazko_e = random.randint(10*60, 150*60)
                for j in range(0, round(dane_zelazko_e)):
                    dane_zelazko_c.append(0)
            if tryb == 2:
                for j in range(0, liczba_wlaczen):
                    if j == 0:
                        temp = random.randrange(55, 65)
                        dane_zelazko_wl.append(temp)
                        for k in range(0, round(temp)):
                            dane_zelazko_c.append(2400)
                    temp = random.gauss(16.58333, 2.712207)
                    dane_zelazko_b.append(temp)
                    for k in range(0, round(temp)):
                        dane_zelazko_c.append(2400)
                    temp = random.weibullvariate(5, 35)
                    dane_zelazko_d.append(temp)
                    for k in range(0, round(temp)):
                        dane_zelazko_c.append(15)
                dane_zelazko_e = random.randint(10*60, 150*60)
                for j in range(0, round(dane_zelazko_e)):
                    dane_zelazko_c.append(0)
            else:
                for j in range(0, liczba_wlaczen):
                    if j == 0:
                        temp = random.randrange(70, 80)
                        dane_zelazko_wl.append(temp)
                        for k in range(0, round(temp)):
                            dane_zelazko_c.append(2400)
                    temp = random.weibullvariate(11, 25)
                    dane_zelazko_b.append(temp)
                    for k in range(0, round(temp)):
                        dane_zelazko_c.append(2400)
                    temp = random.weibullvariate(9, 30)
                    dane_zelazko_d.append(temp)
                    for k in range(0, round(temp)):
                        dane_zelazko_c.append(15)
                dane_zelazko_e = random.randint(10*60, 150*60)
                for j in range(0, round(dane_zelazko_e)):
                    dane_zelazko_c.append(0)
        # dane_zelazko_a = numpy.linspace(0, len(dane_zelazko_c), len(dane_zelazko_c))
        # plt.plot(dane_zelazko_a, dane_zelazko_c)
        # plt.xlabel('Czas [s]')
        # plt.ylabel('Moc [W]')
        # plt.title('Żelazko')
        # plt.show()
        return dane_zelazko_c

    def telewizor(self):
        dane_telewizor_c = []
        liczba_uzyc = random.randint(1, 5)
        for i in range(0, liczba_uzyc):
            dane_telewizor_b = random.lognormvariate(10, 1.9)
            for j in range(0, round(dane_telewizor_b)):
                dane_telewizor_c.append(70)
            dane_telewizor_e = random.randint(30*60, 150*60)
            for j in range(0, round(dane_telewizor_e)):
                dane_telewizor_c.append(26)
        # dane_telewizor_a = numpy.linspace(0, len(dane_telewizor_c), len(dane_telewizor_c))
        # plt.plot(dane_telewizor_a, dane_telewizor_c)
        # plt.xlabel('Czas [s]')
        # plt.ylabel('Moc [W]')
        # plt.title('Telewizor')
        # plt.show()
        return dane_telewizor_c

    def odkurzacz(self):
        dane_odkurzacz_c = []
        liczba_uzyc = random.randint(1, 3)
        liczba_wlaczen = random.randint(1, 3)
        for i in range(0, liczba_uzyc):
            for j in range(0, liczba_wlaczen):
                dane_odkurzacz_b = random.expovariate(0.001)
                for k in range(0, round(dane_odkurzacz_b)):
                    dane_odkurzacz_c.append(600)
                dane_odkurzacz_d = random.gauss(20, 10)
                for k in range(0, round(dane_odkurzacz_d)):
                    dane_odkurzacz_c.append(0)
            dane_odkurzacz_e = random.randint(300*60, 420*60)
            for k in range(0, round(dane_odkurzacz_e)):
                dane_odkurzacz_c.append(0)
        # dane_odkurzacz_a = numpy.linspace(0, len(dane_odkurzacz_c), len(dane_odkurzacz_c))
        # plt.plot(dane_odkurzacz_a, dane_odkurzacz_c)
        # plt.xlabel('Czas [s]')
        # plt.ylabel('Moc [W]')
        # plt.title('Odkurzacz')
        # plt.show()
        return dane_odkurzacz_c

    def oswietlenie(self):
        dane_oswietlenie_c = []
        liczba_wlaczen = random.randint(2, 3)
        for i in range(0, liczba_wlaczen):
            dane_oswietlenie_b = random.gammavariate(60, 90)
            for j in range(0, round(dane_oswietlenie_b)):
                dane_oswietlenie_c.append(8)
            dane_oswietlenie_e = random.randint(30*60, 500*60)
            for j in range(0, round(dane_oswietlenie_e)):
                dane_oswietlenie_c.append(0)
        # dane_oswietlenie_a = numpy.linspace(0, len(dane_oswietlenie_c), len(dane_oswietlenie_c))
        # plt.plot(dane_oswietlenie_a, dane_oswietlenie_c)
        # plt.xlabel('Czas [s]')
        # plt.ylabel('Moc [W]')
        # plt.title('Oswietlenie')
        # plt.show()
        return dane_oswietlenie_c

    def lodowka(self):
        dane_lodowka_c =[]
        dane_lodowka_b = []
        liczba_wlaczen = random.randint(10, 20)
        for i in range(0, 1):
            for j in range(0, liczba_wlaczen):
                dane_lodowka_b = random.gauss(90, 30)
                for k in range(0, round(dane_lodowka_b)):
                    dane_lodowka_c.append(131)
                dane_lodowka_d = random.expovariate(0.00075)
                for k in range(0, round(dane_lodowka_d)):
                    dane_lodowka_c.append(11)
        # dane_lodowka_a = numpy.linspace(0, len(dane_lodowka_c), len(dane_lodowka_c))
        # plt.plot(dane_lodowka_a, dane_lodowka_c)
        # plt.xlabel('Czas [s]')
        # plt.ylabel('Moc [W]')
        # plt.title('Lodowka')
        # plt.show()
        return dane_lodowka_c

    def pralka(self):
        dane_pralka_c =[]
        liczba_wlaczen = random.randint(1, 3)
        for i in range(0, liczba_wlaczen):
            tryb = random.randint(1, 2)
            if tryb == 1:
                for j in range(0, 120):
                    dane_pralka_c.append(40)
                for j in range(0, 120):
                    dane_pralka_c.append(1660)
                for j in range(0, 900):
                    dane_pralka_c.append(300)
                for j in range(0, 240):
                    dane_pralka_c.append(2000)
                for j in range(0, 240):
                    dane_pralka_c.append(40)
                for j in range(0, 120):
                    dane_pralka_c.append(1660)
                for j in range(0, 900):
                    dane_pralka_c.append(300)
                for j in range(0, 360):
                    dane_pralka_c.append(40)
                for j in range(0, 600):
                    dane_pralka_c.append(300)
                dane_pralka_e = random.randint(180*60, 300*60)
                for j in range(0, round(dane_pralka_e)):
                    dane_pralka_c.append(0)
            else:
                for j in range(0, 120):
                    dane_pralka_c.append(40)
                for j in range(0, 180):
                    dane_pralka_c.append(1660)
                for j in range(0, 480):
                    dane_pralka_c.append(300)
                for j in range(0, 600):
                    dane_pralka_c.append(2000)
                for j in range(0, 480):
                    dane_pralka_c.append(300)
                for j in range(0, 60):
                    dane_pralka_c.append(40)
                for j in range(0, 600):
                    dane_pralka_c.append(2000)
                for j in range(0, 900):
                    dane_pralka_c.append(300)
                for j in range(0, 180):
                    dane_pralka_c.append(40)
                for j in range(0, 600):
                    dane_pralka_c.append(300)
                dane_pralka_e = random.randint(180*60, 300*60)
                for j in range(0, round(dane_pralka_e)):
                    dane_pralka_c.append(0)
        # dane_pralka_a = numpy.linspace(0, len(dane_pralka_c), len(dane_pralka_c))
        # plt.plot(dane_pralka_a, dane_pralka_c)
        # plt.xlabel('Czas [s]')
        # plt.ylabel('Moc [W]')
        # plt.title('Pralka')
        # plt.show()
        return dane_pralka_c
