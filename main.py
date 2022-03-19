from enum import Enum, auto
import random


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
def pullFromBag(curBag, pulledAlready, curVal=0):
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


def getBag(bagDict):
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
		Token.Frost: 6,
		Token.Skull: 2,
		Token.Cultist: 2,
		Token.Tablet: 1,
		Token.Tentacle: 1,
		Token.Star: 1,
		Token.Curse: 1
	}

	bag = getBag(bagCount)

	numOfRuns = 100000
	autoFailCount = 0.0
	sumOfResults = 0.0

	for _ in range(numOfRuns):
		autoFailed, val = pullFromBag(bag.copy(), set())

		if autoFailed:
			autoFailCount += 1
		else:
			sumOfResults += val

	print('Auto Fail Percent =', autoFailCount / numOfRuns * 100, '%')
	print('Expected Value =', sumOfResults / (numOfRuns - autoFailCount))
