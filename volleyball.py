import random


def winLose(curTeam):
    if random.random() < curTeam:
        return 1 # represents a round WON
    else:
        return 0  # represents a round LOST


def normalRound(teamOne, teamTwo, curRound, oneScore, twoScore):
    if curRound % 2 != 0:  # when the round number is ODD
        point = winLose(teamOne)  # team one serves on ODD rounds
        if point == 0:
            curRound += 1
        else:
            oneScore += 1
    elif curRound % 2 == 0: # when the round number is EVEN
        point = winLose(teamTwo)# team two serves on EVEN rounds
        if point == 0:
            curRound += 1
        else:
            twoScore += 1
    return curRound, oneScore, twoScore


def rallyRound(teamOne, teamTwo, curRound, oneScore, twoScore):
    if curRound % 2 != 0: # when the round number is ODD
        point = winLose(teamOne)# team one serves on ODD rounds
        if point == 0: # if team one doesn 't score, point is awarded to team two
            twoScore += 1
            curRound += 1
        else:
            oneScore += 1

    elif curRound % 2 == 0:  # when the round number is EVEN# even, teamTwo
        point = winLose(teamTwo)
        if point == 0:  # if team two doesn't score, point is awarded to team one
            oneScore += 1
            curRound += 1
        else:
            twoScore += 1

    return curRound, oneScore, twoScore


def gameDice():
    dice = random.randint(0, 1)
    return dice


def gameSim(maxScore, teamOne, teamTwo):
    oneScore = 0
    twoScore = 0
    curRound = gameDice()  # either 0 or 1. if 0, team two serves first. if 1, team one serves first.
    while (oneScore != maxScore) and(twoScore != maxScore):  # while maxScore(15 or 30) is not reached
        if maxScore == 15:
            curRound, oneScore, twoScore = normalRound(teamOne, teamTwo, curRound, oneScore, twoScore)  # normal mode
        elif maxScore == 30:
            curRound, oneScore, twoScore = rallyRound(teamOne, teamTwo, curRound, oneScore, twoScore)  # rally mode

    if abs(twoScore - oneScore) < 2:  # if game is not won by at least 2 points, continue scoring
        while abs(twoScore - oneScore) < 2:
            if maxScore == 15:
                curRound, oneScore, twoScore = normalRound(teamOne, teamTwo, curRound, oneScore, twoScore)  # normal mode
            elif maxScore == 30:
                curRound, oneScore, twoScore = rallyRound(teamOne, teamTwo, curRound, oneScore, twoScore)  # rally mode

    if twoScore > oneScore:  # if team two wins
        return False
    elif oneScore > twoScore:  # if team one wins
        return True


def userInput():
    teamOne = input("Team One win probability ")
    teamTwo = input("Team Two win probability ")
    numGames = input("Number of games ")
    scoreMode = raw_input("Scoring Mode: normal/rally ")
    return teamOne, teamTwo, numGames, scoreMode


def printDialog(scoreMode, numGames, oneTotalWon, twoTotalWon):
    print "Scoring mode: %s" % scoreMode
    print "Number of games: %s" % numGames
    print "First team: %s wins, %s %%" % (oneTotalWon, (100 * oneTotalWon / numGames))
    print "Second team: %s wins, %s %%" % (twoTotalWon, (100 * twoTotalWon / numGames))


def main():
    teamOne, teamTwo, numGames, scoreMode = userInput()  # gets data

    if scoreMode == "normal":
        maxScore = 15
    elif scoreMode == "rally":
        maxScore = 30

    oneTotalWon = 0
    twoTotalWon = 0
    for i in range(numGames):
        whoWon = gameSim(maxScore, teamOne, teamTwo)
        if whoWon is True:  # if team one wins
            oneTotalWon += 1
        elif not whoWon:  # if team two wins
            twoTotalWon += 1

    printDialog(scoreMode, numGames, oneTotalWon, twoTotalWon)
    print "online master"

main()
