from enum import Enum, auto


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
    Token.Blessing: 2
}

if __name__ == '__main__':
    pass
