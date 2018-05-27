import Urzadzenia
import Urzadzenia_multi
import matplotlib.pyplot as plt
import random
import numpy

def czy_uzywane():
    uzywane = False
    if random.random() > 0.85:
        uzywane = True
    return uzywane


def liczba_gniazdek(nazwa_pomieszczenia):
    return pomieszczenia_ograniczenie[nazwa_pomieszczenia]


def losuj_pomieszczenie(wszystkie_pomieszczenia):
    return random.choice(wszystkie_pomieszczenia)


def losuj_urzadzenie(nazwa_pomieszczenia):
    if nazwa_pomieszczenia == 'pokoj':
        temp = random.randint(1, 4)
        if temp == 1:
            tryb = random.randint(1, 3)
            a = random.randint(0, 3*60*60)
            e = random.randint(1.5*60*60, 5*60*60)
            if tryb == 1:
                c = random.gauss(7.85, 1.5)
                d = random.expovariate(0.05)
            elif tryb == 2:
                c = random.gauss(16.58333, 2.712207)
                d = random.weibullvariate(5, 35)
            else:
                c = random.weibullvariate(11, 25)
                d = random.weibullvariate(9, 30)
            parametr_b = Urzadzenia_multi.zelazko(a, c, d, e)
            urzadzenie = 'zelazko'
        elif temp == 2:
            a = random.randint(1*60*60, 10*60*60)
            c = random.gammavariate(60, 90)
            e = random.randint(5000, 10000)
            parametr_b = Urzadzenia_multi.oswietlenie(a, c, e)
            urzadzenie = 'oswietlenie'
        elif temp == 3:
            a = random.randint(300, 1000)
            c = random.expovariate(0.001)
            d = random.gauss(20, 10)
            e = random.randint(1000, 2000)
            parametr_b = Urzadzenia_multi.odkurzacz(a, c, d, e)
            urzadzenie = 'odkurzacz'
        else:
            a = random.randint(0, 1000)
            c = random.lognormvariate(10, 1.9)
            e = random.randint(180, 900)
            parametr_b = Urzadzenia_multi.telewizor(a, c, e)
            urzadzenie = 'telewizor'
    if nazwa_pomieszczenia == 'przedpokoj':
        temp = random.randint(1, 3)
        if temp == 1:
            a = random.randint(0, 4*60*60)
            c = random.expovariate(0.001)
            d = random.gauss(20, 10)
            e = random.randint(2*60*60, 4*60*60)
            parametr_b = Urzadzenia_multi.odkurzacz(a, c, d, e)
            urzadzenie = 'odkurzacz'
        elif temp == 2:
            a = random.randint(0, 2*60*60)
            c = random.gammavariate(1*60*60, 1.5*60*60)
            e = random.randint(5000, 10000)
            parametr_b = Urzadzenia_multi.oswietlenie(a, c, e)
            urzadzenie = 'oswietlenie'
        else:
            tryb = random.randint(1, 3)
            a = random.randint(0, 10*60*60)
            e = random.randint(50*60*60, 300*60*60)
            if tryb == 1:
                c = random.gauss(7.85, 1.5)
                d = random.expovariate(0.05)
            elif tryb == 2:
                c = random.gauss(16.58333, 2.712207)
                d = random.weibullvariate(5, 35)
            else:
                c = random.weibullvariate(11, 25)
                d = random.weibullvariate(9, 30)
            parametr_b = Urzadzenia_multi.zelazko(a, c, d, e)
            urzadzenie = 'zelazko'
    if nazwa_pomieszczenia == 'kuchnia':
        temp = random.randint(1, 3)
        if temp == 1:
            a = random.randint(2000, 3500)
            c = random.gammavariate(60, 90)
            e = random.randint(5000, 10000)
            parametr_b = Urzadzenia_multi.oswietlenie(a, c, e)
            urzadzenie = 'oswietlenie'
        elif temp == 2:
            a = random.randint(300, 1000)
            c = random.expovariate(0.001)
            d = random.gauss(20, 10)
            e = random.randint(1000, 2000)
            parametr_b = Urzadzenia_multi.odkurzacz(a, c, d, e)
            urzadzenie = 'odkurzacz'
        else:
            a = 0
            c = random.gauss(90, 30)
            d = random.expovariate(0.00075)
            e = 0
            parametr_b = Urzadzenia_multi.lodowka(a, c, d, e)
            urzadzenie = 'lodowka'
    if nazwa_pomieszczenia == 'lazienka':
        temp = random.randint(1, 2)
        if temp == 1:
            a = random.randint(2000, 3500)
            c = random.gammavariate(60, 90)
            e = random.randint(5000, 10000)
            parametr_b = Urzadzenia_multi.oswietlenie(a, c, e)
            urzadzenie = 'oswietlenie'
        else:
            a = random.randint(0, 5*60*60)
            e = random.randint(0, 72*60*60)
            parametr_b = Urzadzenia_multi.pralka(a, e)
            urzadzenie = 'pralka'
    return urzadzenie, parametr_b


pomieszczenia_ograniczenie = {'pokoj': 6, 'przedpokoj': 2, 'kuchnia': 5, 'lazienka': 2}
urzadzenia_ograniczenie = {'zelazko': 1, 'odkurzacz': 1, 'telewizor': 2, 'oswietlenie': 5, 'pralka': 1, 'lodowka': 1}
indeks = 0
parametr_b = []
czas = []
ilosc_budynkow = input('Podaj liczbę budynków: ')
ilosc_kondygnacji = input('\nPodaj liczbę kondygnacji: ')
ilosc_mieszkan = input('\nPodaj liczbę mieszkań: ')
ilosc_pomieszczen = input('\nPodaj liczbę pomieszczeń: ')

for i in range(0, int(ilosc_budynkow)):
    for j in range(0, int(ilosc_kondygnacji)):
        for k in range(0, int(ilosc_mieszkan)):
            wszystkie_pomieszczenia = ['pokoj', 'pokoj', 'przedpokoj', 'kuchnia', 'lazienka']
            for l in range(0, int(ilosc_pomieszczen)):
                pomieszczenie = losuj_pomieszczenie(wszystkie_pomieszczenia)
                ilosc_gniazdek = liczba_gniazdek(pomieszczenie)
                wszystkie_pomieszczenia.remove(pomieszczenie)
                for m in range(0, ilosc_gniazdek):
                    uzywane = czy_uzywane()
                    if uzywane:
                        temp = losuj_urzadzenie(pomieszczenie)
                        parametr_b.append(temp[1])
                        czas.append(len(parametr_b[indeks]))
                        indeks += 1
dane_b = []
suma = 0
zakres = 1*60*60
# if len(czas) != 0:
#     zakres = max(czas)
for i in range(0, zakres):
    for j in range(0, len(parametr_b)):
        if i <= len(parametr_b[j]) - 1:
            temp = parametr_b[j][i]
            suma = suma + temp
    dane_b.append(suma)
    suma = 0
dane_a = numpy.linspace(0, len(dane_b), len(dane_b))
plt.plot(dane_a, dane_b)
plt.title('Agregacja danych')
plt.xlabel('Czas [s]')
plt.ylabel('Moc [W]')
plt.savefig('images/wykres1.png')