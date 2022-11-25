import numpy as np

DECK_SIZE = 31
cardsOfInterest = 5

trails = 10000
inTopTenCount = 0

for _ in range(trails):
	deck = [1 for _ in range(cardsOfInterest)]
	deck += [0 for _ in range(DECK_SIZE - cardsOfInterest)]
	np.random.shuffle(deck)

	if 1 in deck[:10]:
		inTopTenCount += 1

print(inTopTenCount / trails)
