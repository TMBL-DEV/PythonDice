import random


class Game:
    __score = 100
    __tries = 5
    __round = 0
    __dice = 0
    __history = []

    def getRound(self):
        return self.__round

    def getTries(self):
        return self.__tries

    def getScore(self):
        return self.__score

    def rollDice(self):
        self.__dice = random.randint(1, 6)
        return self.__dice

    def guessDice(self, guess):
        if int(guess) == self.__dice:
            self.__score += 50
            return True

        self.__score -= 20
        return False

    def getDice(self):
        return self.__dice

    def endRound(self):
        self.__round += 1
        self.__dice = 0


def gameTime():

    game = Game()
    attempts = int(game.getTries())
    print("U heeft nog " + str(game.getTries()) + " pogingen")

    for attempt in range(attempts):
        print("U score is " + str(game.getScore()))
        print("wat denkt u dat de dobbelsteen is?")
        guess = input(" getal 1 t/m 6 mag u gebruiken \n")
        game.rollDice()
        result = game.guessDice(guess)

        if result:
            print("Dat klopt!!!")
        else:
            print("Dat heeft u fout, en dat gaat u kosten")
            print("het was " + str(game.getDice()))

        game.endRound()

    print("u score is " + str(game.getScore()))
    print("gg")


print("opties: gokken, rollen")
choice = input("Wilt u gokken, of alleen rollen? \n")

if choice == "gokken":
    gameTime()

if choice == "rollen":
    game = Game()
    print("de dobbelsteen is: " + str(game.rollDice()))
