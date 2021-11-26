import json
import random

def credits(infoPath):
    """Prints the credits but requires a .json file"""
    with open(infoPath, 'r') as myfile:
        info = myfile.read()
    title = json.loads(info)

    print("-------------------------------")
    print(title["title"])
    print("\tBy",title["author"])
    print("\tDate Last Modified", title["dateModified"])
    print("-------------------------------")

def creditsNoJSON():
    """Prints the credits without .json file"""
    print("-------------------------------")
    print("DiceGame")
    print("\tBy Humberto Rendon")
    print("-------------------------------")

def createDice(totalSides):
    """Return a dice dictionary with n amount of sides"""
    return { "sides": totalSides }


def getRandomNumber(dice):
    """Returns a random integer between 1 and the sides of the dice"""
    return random.randint(1,dice["sides"])


def rollDiceList(dice, num):
    """Returns a list of random integer between 1 and the sides of the dice"""
    return [getRandomNumber(dice) for i in range(0,num) ]


def rollDiceOnce(dice):
    """Returns a list of random integer between 1 and the sides of the dice"""
    return rollDiceList(dice,1)

def getDiceRollsMode(diceRollList):
    rollDict = {}
    maxCount = 0
    maxRoll = ""

    for roll in diceRollList:
        if str(roll) not in rollDict:
            rollDict[str(roll)] = 1
        else:
            rollDict[str(roll)] += 1

        if rollDict[str(roll)] > maxCount:
            maxCount = rollDict[str(roll)]
            maxRoll = str(roll)

    return (maxRoll, maxCount)

def getDiceRollsSum(diceRollList):
    """Returns the sum from a list of dice rolls"""
    sum = 0
    for roll in diceRollList:
        sum += roll

    return sum

def getDiceRollsMean(diceRollList):
    """Returns the mean from the list of dice rolls"""
    sum = getDiceRollsSum(diceRollList)
    return sum / len(diceRollList)

def printDiceRolls(diceRollList):
    """Prints the list of dice rolls"""
    rollNum = 1
    for roll in diceRollList:
        print(f"Roll #{rollNum}: {roll}")
        rollNum += 1

def csvRollList(fileName,diceRollList):
    """Converts the list of dice rolls into a .csv file"""
    f = open(str(fileName+".csv"),"w")
    f.write("rollNum, rollResult\n")
    rollNum = 1

    for roll in diceRollList:
        f.write(f"{rollNum}, {roll}\n")
        rollNum += 1
    f.close()

def txtRollList(fileName,diceRollList):
    """Converts the list of dice rolls into a .txt file"""
    f = open(str(fileName+".txt"),"w")
    rollNum = 1

    for roll in diceRollList:
        f.write(f"Roll #{rollNum}: {roll}\n")
        rollNum += 1

    f.close()


def TestSimpleDiceGame():
    """A simple test of the game"""
    # Calling functions
    creditsNoJSON()
    myDice = createDice(6)
    timesRolled = 50
    rollList = rollDiceList(myDice,timesRolled)
    csvRollList("rollList",rollList)
    txtRollList("rollList",rollList)

def menuChoice():
    creditsNoJSON()
    print("[ 1 ] Create Dice")
    print("[ 2 ] Roll Regular 6 Side Dice Once")
    print("[ R ] Repeat Message")
    print("[ Q ] Quit")
    print("-------------------------------")

    ans = input().lower()
    print("-------------------------------")


    while True:

        if ans == "1":
            createGame()
        elif ans == "2":
            rollList = rollDiceOnce(createDice(6))
            printDiceRolls(rollList)
            print("-------------------------------")
            print("[ 1 ] Create Dice")
            print("[ 2 ] Roll Regular 6 Side Dice Once")
            print("[ R ] Repeat Message")
            print("[ Q ] Quit")
        elif ans == "r":
            print("-------------------------------")
            print("[ 1 ] Create Dice")
            print("[ 2 ] Roll Regular 6 Side Dice Once")
            print("[ R ] Repeat Message")
            print("[ Q ] Quit")
        elif ans == "q":
            break
        else:
            print("-------------------------------")
            print("Invalid Choice")
            print("-------------------------------")

        ans = input().lower()
        print("-------------------------------")


def createGame():
    sides = int(input("Pick the number of sides for the dice: "))
    myDice = createDice(sides)
    timesRolled = int(input("How many times do you wan to roll the dice: "))
    rollList = rollDiceList(myDice, timesRolled)
    print("-------------------------------")
    printDiceRolls(rollList)
    print("-------------------------------")

    txtAns = input("Write to an .txt file? ").lower()
    csvAns = input("Write to an .csv file? ").lower()

    if txtAns == "y" or txtAns == "yes":
        txtRollList("rollListT", rollList)
    
    if csvAns == "y" or csvAns == "yes":
        csvRollList("rollListC", rollList)


if __name__ == '__main__':
    menuChoice()