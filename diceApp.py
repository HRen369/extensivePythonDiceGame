import json
import random

def credits(infoPath):
    with open(infoPath, 'r') as myfile:
        info = myfile.read()
    title = json.loads(info)

    print("-------------------------------")
    print(title["title"])
    print("\tBy",title["author"])
    print("-------------------------------")

def creditsNoJSON():
    print("-------------------------------")
    print("DiceGame")
    print("\tBy Humberto Rendon")
    print("-------------------------------")

def createDice(totalSides):
    return {
        "sides": totalSides
    }


def getRandomNumber(dice):
    return random.randint(1,dice["sides"])


def rollDiceList(dice, num):
    return [getRandomNumber(dice) for i in range(0,num) ]


def rollDiceOnce(dice):
    return rollDiceList(dice,1)

##******
def getDiceRollsMode(diceRollList):
    diceRollList.sort()
    currentModeTotal = 0
    mode = 0

    for i in range(len(rollDiceList)-1):
        if rollDiceList[i] == rollDiceList[i+1]:
            mode += 1

def getDiceRollsSum(diceRollList):
    sum = 0
    for roll in diceRollList:
        sum += roll

    return sum

def getDiceRollsMean(diceRollList):
    sum = getDiceRollsSum(diceRollList)
    return sum / len(diceRollList)

def printDiceRolls(diceRollList):
    rollNum = 1
    for roll in diceRollList:
        print(f"Roll #{rollNum}: {roll}")
        rollNum += 1

def csvRollList(fileName,diceRollList):
    f = open(str(fileName+".csv"),"w")
    f.write("rollNum, rollResult\n")
    rollNum = 1

    for roll in diceRollList:
        f.write(f"{rollNum}, {roll}\n")
        rollNum += 1
    f.close()

def txtRollList(fileName,diceRollList):
    f = open(str(fileName+".txt"),"w")
    rollNum = 1

    for roll in diceRollList:
        f.write(f"Roll #{rollNum}: {roll}\n")
        rollNum += 1

    f.close()


def simpleDiceGameTest():
    # Calling functions
    creditsNoJSON()
    myDice = createDice(6)
    timesRolled = 50
    rollList = rollDiceList(myDice,timesRolled)
    printDiceRolls(rollList)
    csvRollList("rollList",rollList)
    txtRollList("rollList",rollList)

def menuChoice():
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
    pass

menuChoice()



"""
myDice = int(input("Pick the number of sides for the dice"))
timesRolled = int(input("How many times do you wan to roll the dice"))




"""