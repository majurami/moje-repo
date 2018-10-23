#pobiera moduł random
import random

koszyczek = ['a','b','c','d','yeti','zebra','w','u','coco','pomarancza']
team1 = []
#len zwraca dlugosc listy
pojemnoscKoszyczka = len(koszyczek)
# podzieli pojemnoscKoszyczka przez 2 i wynikiem bedzie liczba calkowita(int)
polowa = pojemnoscKoszyczka // 2 

for liczba in range(polowa):
    #wylosuje element z isty koszyczek
    losowyElement = random.choice(koszyczek)
    team1.append(losowyElement)
    koszyczek.remove(losowyElement)
print('Team 1:', team1)
print('Team 2:', koszyczek)
