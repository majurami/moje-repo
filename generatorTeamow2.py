#pobiera moduł random
import random

koszyczek = ['a','b','c','d','yeti','zebra','w','u','coco','pomarancza']

random.shuffle(koszyczek)
polowa = len(koszyczek)//2
team1 = koszyczek[ 0 : polowa]
team2 = koszyczek [polowa : ]
print('Team 1:', team1)
print('Team 2:', team2)