from collections import defaultdict
from enum import Enum, auto
import random
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class Token(Enum):
	PlusOne = auto()
	Zero = auto()
	MinusOne = auto()
	MinusTwo = auto()
	MinusThree = auto()
	MinusFour = auto()
	MinusFive = auto()
	MinusSix = auto()
	MinusSeven = auto()
	MinusEight = auto()
	Cultist = auto()
	Skull = auto()
	Tablet = auto()
	ElderThing = auto()
	Tentacle = auto()
	Frost = auto()
	Curse = auto()
	Blessing = auto()
	Star = auto()


tokenValues = {
	Token.PlusOne: 1,
	Token.Zero: 0,
	Token.MinusOne: -1,
	Token.MinusTwo: -2,
	Token.MinusThree: -3,
	Token.MinusFour: -4,
	Token.MinusFive: -5,
	Token.MinusSix: -6,
	Token.MinusSeven: -7,
	Token.MinusEight: -8,
	Token.Cultist: -2,
	Token.Skull: -4,
	Token.Tablet: -3,
	Token.ElderThing: -4,
	Token.Frost: -1,
	Token.Curse: -2,
	Token.Blessing: 2,
	Token.Star: 1
}

pullAgainTypes = {
	Token.Frost,
	Token.Blessing,
	Token.Curse
}


# Returns a tuple of a boolean and an int
# If the boolean is True then this pull is an auto fail
# If the boolean is False, then the int is the result of this pull
def pullFromBag(curBag: list, pulledAlready: set, curVal: int = 0) -> (bool, int):
	tokenIndex = random.randint(0, len(curBag) - 1)

	token = curBag[tokenIndex]
	curBag.remove(token)

	if token == Token.Tentacle or (token == Token.Frost and Token.Frost in pulledAlready):
		return True, 0

	curVal += tokenValues[token]
	pulledAlready.add(token)

	if token in pullAgainTypes:
		return pullFromBag(curBag, pulledAlready, curVal)
	else:
		return False, curVal


def getBag(bagDict: dict) -> list:
	tempBag = []

	for key in bagCount:
		tempBag += [key for _ in range(bagDict[key])]

	return tempBag


if __name__ == '__main__':
	bagCount = {
		Token.Zero: 2,
		Token.MinusOne: 2,
		Token.MinusTwo: 2,
		Token.MinusThree: 1,
		Token.MinusFour: 2,
		Token.MinusFive: 1,
		Token.Frost: 0,
		Token.Skull: 2,
		Token.Cultist: 2,
		Token.Tablet: 1,
		Token.Tentacle: 1,
		Token.Star: 1,
		Token.Curse: 0
	}

	bag = getBag(bagCount)

	numOfRuns = 100000
	autoFailCount = 0.0
	sumOfResults = 0.0

	valDict = defaultdict(int)

	resultCounts = defaultdict(int)

	for _ in range(numOfRuns):
		autoFailed, val = pullFromBag(bag.copy(), set())

		resultCounts[val] += 1

		if autoFailed:
			autoFailCount += 1
		else:
			sumOfResults += val

	autoFailChance = autoFailCount / numOfRuns
	expectedValue = sumOfResults / (numOfRuns - autoFailCount)

	print('Auto Fail Percent =', autoFailChance * 100, '%')
	print('Expected Value =', expectedValue)

	resultVals = sorted(list(resultCounts))
	percents = [(resultCounts[result] / numOfRuns) - (resultCounts[result] / numOfRuns * autoFailChance)
				for result in resultVals]

	for i in range(len(percents) - 2, -1, -1):
		percents[i] = percents[i] + percents[i + 1]

	data = {
		"y": percents,
		"x": resultVals
	}

	df = pd.DataFrame(data)

	print(df)
	plt.grid()
	sns.lineplot(data=df, y="y", x="x")
	# plt.xticks(resultVals)
	plt.xticks(resultVals[::2])
	plt.yticks([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0])
	plt.xlabel("Value of Bag Pull")
	plt.ylabel("Likelihood")
	plt.title("Chance of >= Value From Bag Pull")
	plt.scatter(df['x'], df['y'], zorder=1)
	plt.show()
