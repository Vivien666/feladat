import random
lista = list(range(1,91))
kihuzott = []
for x in range(5):
	szam = random.choice(lista)
	lista.remove(szam)
	kihuzott.append(str(szam))
print("Huzott számok:"+" ".join(kihuzott))
