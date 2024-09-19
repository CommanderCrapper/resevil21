import random
import time

# Pedro actually had a really cool idea about "fake" trump cards, where a trump card can be drawn for the other person where it has the inverse effect of what is actually on the card. 

playerCards = []
botCards = []
playerValue = 0
botValue = 0

playerHand = []
botHand = []

# status of player/bot, 0 means active & 1 means settled
playerStatus = 0
botStatus = 0
choice = None

usedCards = []

playerTrumpList = []
botTrumpList = []

turn = 0

use = 0

def playerTurn():
    playerTrumpDisplay = []
    # Display options, ask for input, follow from there
    optionsList = ['trump', 'hit', 'stay']
    choice = input('What will you do? (Type "trump", "hit" or "stay". Choices are case-sensitive, so make sure you type them correctly!)')
    if (choice in optionsList) == False:
        playerTurn()
    if choice == 'trump':
        # fix this part
        for i in playerTrumpList:
            playerTrumpDisplay.append(i)
        print('Your trump cards: ', playerTrumpDisplay, '\n' '\n')
        print('ID LIST & FUNCTIONS:', '\n', 'id 0-4 = draw 3-7', '\n', 'id 5 = remove opponent card', '\n', 'id 6 = remove last card for you', '\n', 'id 7 = swap latest cards with bot', '\n', 'id 8 = get rid of 2 random trump cards & draw 3 new ones', '\n', 'id 9 = draw perfect card to reach 21 (if available)', '\n', 'id 10 = both you & your opponent draw a trump card')
        choice2 = input('What trump card will you use? (type the ID (starting from 0) of the trump card you want to use, or type "back" to return to the previous menu)')
        if(choice2 == 'back'):
            playerTurn()
        if (choice2 in playerTrumpList) == False:
            choice2 = input('Trump card not in the list! Please input a valid response. Type "back" to return to the previous menu if needed.')
        if choice2 == 'back':
            playerTurn()
        elif choice == 'hit':
            drawPlayer()
            playerStatus = 0
            botStatus = 0
        elif choice == 'stay':
            playerStatus = 1
        else:
            playerTurn()
        if botStatus == 0:
            turn = 1
        if playerStatus == 1 and botStatus == 1:
            showdown()

# Do I have to add the variables used below as a parameter?
def startGame(turn):
    playerCards = []
    botCards = []
    playerValue = 0
    botValue = 0
    usedCards = []
    drawPlayer(playerValue)
    drawPlayer(playerValue)
    drawBot(botValue)
    drawBot(botValue)
    # give turn to opposite player when new game starts
    if turn == 0:
        turn = 1
    elif turn == 1:
        turn = 0

def drawPlayer(playerValue):
    use = 0
    failCount = 0
    randomNum = random.randrange(1,11)
    if (randomNum in usedCards) or (randomNum in botCards):
        while (randomNum in playerCards) or (randomNum in botCards):
            randomNum = random.randrange(1,11)
            failCount += 1
            if failCount == 20:
                use = -1
                break
    
    if use != -1:
        trumpCheck()
        playerCards.append(randomNum)
        playerValue = playerValue + randomNum
        usedCards.append(randomNum)
        turn = 1

def drawBot(botValue):
    randomNum = random.randrange(1,11)
    if (randomNum in usedCards) or (randomNum in botCards):
        while (randomNum in playerCards) or (randomNum in botCards):
            randomNum = random.randrange(1,11)
    
    trumpCheck()
    botCards.append(randomNum)
    botValue = botValue + randomNum
    usedCards.append(randomNum)
    turn = 0

def updateScreen():
    botDeckShown = []
    botValue = 0
    botValue2 = 0
    for i in botCards:
        current = botCards.index(i)
        if current == 0:
            botDeckShown.append('?')
            botValue += i
        elif current != 0:
            botDeckShown.append(i)
            botValue += i
            botValue2 += i
    
    print('Bot deck: ', botDeckShown, '\n' + '\n')
    print('Bot total: ', '? + ', botValue2)
    
    print('\n', '\n', '\n')

    playerValue = 0
    playerCards2 = []
    for i in playerCards:
        current = playerCards.index(i)
        playerValue += i
        playerCards2.append(i)
    
    print('Your hand: ', playerCards, '\n')
    print('Total: ', playerValue)

def trumpCheck():
    determinant = random.randrange(1,10)
    if determinant == 5:
        randomNum = random.randrange(0,11)
        if turn == 0:
            playerTrumpList.append(randomNum)
            print('appended ', randomNum, 'to playerTrumpList')
        else:
            botTrumpList.append(randomNum)
            print('appended ', randomNum, 'to botTrumpList')


def showdown():
    timeDelay = random.randrange(3,7)
    if playerValue == botValue:
        updateScreen()
        print("The winner is...")
        time.sleep(timeDelay)
        if playerValue == botValue:
            print("It's a... DRAW!")
        elif playerValue == 21:
            print("CLANCY!!!")
        elif botValue == 21:
            print("HOFFMAN!!!")
        elif playerValue > botValue and playerValue < 21:
            print('CLANCY!!!')
        elif playerValue < botValue and botValue < 21:
            print('HOFFMAN!!!')
        elif playerValue > 21 and botValue > 21:
            if playerValue < botValue:
                print('CLANCY!!!')
            else:
                print('HOFFMAN!!!')

def draw3():
    if turn == 0:
        if usedCards.includes(3):
            # Does nothing
            print('3 is not in the deck, trump card discarded.')
        else:
            playerHand.append(3)
            usedCards.append(3)
            usedTrump = playerTrumpList.findIndexOf(0)
            playerTrumpList.pop(usedTrump)
    if turn == 1:
        if usedCards.includes(3):
        # Does nothing
            print('3 is not in the deck, trump card discarded')
        else: 
            botHand.append(3)
            usedCards.append(3)
            usedTrump = botTrumpList.findIndexOf(0)
            botTrumpList.pop(usedTrump)
    updateScreen()

def draw4():
    if turn == 0:
        if usedCards.includes(4):
            # Does nothing
            print('4 is not in the deck, trump card discarded.')
        else:
            playerHand.append(4)
            usedCards.append(4)
            usedTrump = playerTrumpList.findIndexOf(1)
            playerTrumpList.pop(usedTrump)
    if turn == 1:
        if usedCards.includes(4):
        # Does nothing
            print('4 is not in the deck, trump card discarded')
        else: 
            botHand.append(4)
            usedCards.append(4)
            usedTrump = botTrumpList.findIndexOf(1)
            botTrumpList.pop(usedTrump)
    updateScreen()

def draw5():
    if turn == 0:
        if usedCards.includes(5):
            # Does nothing
            print('5 is not in the deck, trump card discarded.')
        else:
            playerHand.append(5)
            usedCards.append(5)
            usedTrump = playerTrumpList.findIndexOf(2)
            playerTrumpList.pop(usedTrump)
    if turn == 1:
        if usedCards.includes(5):
        # Does nothing
            print('5 is not in the deck, trump card discarded')
        else: 
            botHand.append(5)
            usedCards.append(5)
            usedTrump = botTrumpList.findIndexOf(2)
            botTrumpList.pop(usedTrump)
    updateScreen()

def draw6():
    if turn == 0:
        if usedCards.includes(6):
            # Does nothing
            print('6 is not in the deck, trump card discarded.')
        else:
            playerHand.append(6)
            usedCards.append(6)
            usedTrump = playerTrumpList.findIndexOf(3)
            playerTrumpList.pop(usedTrump)
    if turn == 1:
        if usedCards.includes(6):
        # Does nothing
            print('6 is not in the deck, trump card discarded')
        else: 
            botHand.append(6)
            usedCards.append(6)
            usedTrump = botTrumpList.findIndexOf(3)
            botTrumpList.pop(usedTrump)
    updateScreen()

def draw7():
    if turn == 0:
        if usedCards.includes(7):
            # Does nothing
            print('5 is not in the deck, trump card discarded.')
        else:
            playerHand.append(7)
            usedCards.append(7)
            usedTrump = playerTrumpList.findIndexOf(4)
            playerTrumpList.pop(usedTrump)
    if turn == 1:
        if usedCards.includes(7):
        # Does nothing
            print('7 is not in the deck, trump card discarded')
        else: 
            botHand.append(7)
            usedCards.append(7)
            usedTrump = botTrumpList.findIndexOf(4)
            botTrumpList.pop(usedTrump)
    updateScreen()

def removeCard():
    if turn == 0:
        removedCard = botCards.pop()
        usedCards.append(removedCard)
        usedTrump = playerTrumpList.findIndexOf(5)
        playerTrumpList.pop(usedTrump)
    else:
        removedCard = playerCards.pop()
        usedCards.append(removedCard)
        usedTrump = botTrumpList.findIndexOf(5)
        playerTrumpList.pop(usedTrump)
    updateScreen()

def returnCard():
    if turn == 0:
        removedCard = playerCards.pop()
        usedCards.append(removedCard)
        usedTrump = playerTrumpList.findIndexOf(6)
        playerTrumpList.pop(usedTrump)
    else:
        removedCard = botCards.pop()
        usedCards.append(removedCard)
        usedTrump = botTrumpList.findIndexOf(6)
        playerTrumpList.pop(usedTrump)
    updateScreen()

def exchangeCard():
    cardSwap1 = playerCards.pop()
    cardSwap2 = botCards.pop()
    botCards.append(cardSwap1)
    playerCards.append(cardSwap2)
    if turn == 0:
        usedTrump = playerTrumpList.findIndexOf(7)
        playerTrumpList.pop(usedTrump)
    else:
        usedTrump = playerTrumpList.findIndexOf(7)
        playerTrumpList.pop(usedTrump)
    updateScreen()

def trumpSwitch():
    random1 = 0
    random2 = 0
    if turn == 0:
        random1 = random.randrange(0, len(playerTrumpList))
        random2 = random.randrange(0, len(playerTrumpList))
        playerTrumpList.pop(random1)
        playerTrumpList.pop(random2)
        # Not entirely sure how to do for loops for a specified amount instead of smth like "for x in length of this list"
        for i in 3:
            randomNum = random.randrange(1,11)
            playerTrumpList.append(randomNum)
        usedTrump = playerTrumpList.findIndexOf(8)
        playerTrumpList.pop(usedTrump)
    else:
        random1 = random.randrange(0, len(botTrumpList))
        random2 = random.randrange(0, len(botTrumpList))
        botTrumpList.pop(random1)
        botTrumpList.pop(random2)
        for i in 3:
            random = random.randrange(0,11)
            botTrumpList.append(randomNum)
        usedTrump = botTrumpList.findIndexOf(8)
        botTrumpList.pop(usedTrump)

def drawPerfect():
    if turn == 0:
        perfectCard = 21 - playerValue
        if usedCards.includes(perfectCard):
            playerHand.append(perfectCard)
            usedCards.append(perfectCard)
            usedTrump = playerTrumpList.findIndexOf(9)
            playerTrumpList.pop(usedTrump)
        else:
            while usedCards.includes(perfectDraw):
                perfectDraw = perfectDraw - 1
            playerHand.append(perfectDraw)
            usedCards.append(perfectDraw)
            usedTrump = playerTrumpList.findIndexOf(9)
            playerTrumpList.pop(usedTrump)
    else:
        perfectCard = 21 - botValue
        if usedCards.includes(perfectDraw):
            botHand.append(perfectDraw)
            usedCards.append(perfectDraw)
            usedTrump = botTrumpList.findIndexOf(9)
            botTrumpList.pop(usedTrump)
        else:
            while usedCards.includes(perfectDraw):
                botDraw = perfectDraw - 1
        botHand.append(perfectDraw)
        usedCards.append(perfectDraw)
        usedTrump = playerTrumpList.findIndexOf(9)
        botTrumpList.pop(usedTrump)
    updateScreen()

def happiness():
    randomNum = random.randrange(0,10)
    playerTrumpList.append(randomNum)
    botTrumpList.append(randomNum)
    if turn == 0:
        playerTrumpList.findIndexOf(10)
        playerTrumpList.pop(10)
    else:
        botTrumpList.findIndexOf(10)
        botTrumpList.pop(10)

startGame(turn)

# HERE'S the actual game stuff that determines when the game is active & whatnot
while playerStatus == 0 or botStatus == 0:
    updateScreen()
    failCount = 0
    # game is active
    if turn == 1:
        if botValue != 21:
            # random chance to use any trump card as long as it isn't one that draws a card
            determinant = random.randrange(1, 10)
            if determinant == 10:
                use = random.randrange(1, 4)
                if botTrumpList.includes(use) == False:
                    use = random.randrange(1, 4)
                    failCount += 1
                    if failCount == 20:
                        use = -1
                        break
            if use == 1:
                removeCard()
            elif use == 2:
                returnCard()
            elif use == 3:
                exchangeCard()
            elif use == 4:
                trumpSwitch()
        # draws perfect if parameters are met
        if botValue > 10 and botTrumpList.includes(9) and botValue != 21:
            determinant = random.randrange(1, 10)
            if determinant == 10:
                drawPerfect()
            
        # draws 7 if parameters are met
        if botValue == 14 and botTrumpList.includes(4):
            if usedCards.findIndexOf(7) == False:
                determinant = random.randrange(1,10)
                if determinant == 10:
                    draw7()

        # draws 6 if parameters are met
        if botValue == 15 and botTrumpList.includes(3):
            if usedCards.findIndexOf(6) == False:
                determinant = random.randRange(1,10)
                if determinant == 10:
                    draw6()
        
        # Draws 5 if parameters are met
        if botValue == 16 and botTrumpList.includes(2):
            if usedCards.findIndexOf(5) == False:
                determinant = random.randrange(1,10)
                if determinant == 10:
                    draw5()
        
        # Draws 4 if parameters are met
        if botValue == 17 and botTrumpList.includes(1):
            if usedCards.findIndexOf(4) == False:
                determinant = random.randrange(1,10)
                if determinant == 10:
                    draw4()
        
        # Draws 3 if parameters are met
        if botValue == 18 and botTrumpList.includes(0):
            if usedCards.findIndexOf(3) == False:
                determinant = random.randrange(1,10)
                if determinant == 10:
                    draw3()

        # Checks values & bases next move off current value
        if botValue > 21:
            if botTrumpList.includes(6):
                returnCard()
            else:
                botStatus = 1
                turn = 0
        
        if botValue == 21:
            botStatus = 1
        elif botValue >= 17:
            botStatus = 1
        elif botValue >= 13 or botValue <= 16:
            determinant = random.randrange(0,1)
            if determinant == 1:
                # fuck it we ball
                drawBot()
            else:
                botStatus = 1
                turn = 0
        elif botValue < 13:
            drawBot()
            botStatus = 0
            turn = 0
        turn = 0
        updateScreen()
    else:
        playerTurn()