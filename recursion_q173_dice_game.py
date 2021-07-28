def diceStreakGamble(player1,player2,player3,player4):
    players = [player1, player2, player3, player4]
    winner = 0
    winnerMoney = 0
    winnerArr = []
    for i, player in enumerate(players):
        if diceStreakGambleHelper(player) > winnerMoney:
            winner = i + 1
            winnerMoney = diceStreakGambleHelper(player)
            winnerArr = player
    
    print("Winner: Player " + str(winner) + " won $" + str(winnerMoney) + " by rolling " + str(winnerArr))




def diceStreakGambleHelper(arr):
    maxValue = arr[0]
    getMoney = 4
    for i in range(1, len(arr)):
        if arr[i] < maxValue: getMoney = 0
        getMoney += 4
    
    return getMoney

diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,4])
diceStreakGamble([1,2,3,-1,4,5],[3,4,2],[4,2,4],[6,16,4])
diceStreakGamble([4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1])
diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,26])
diceStreakGamble([1,2,1],[3,4,2],[4,2,4],[6,16,26])
diceStreakGamble([5,19,19,20],[23,23,32,5],[20,23,30,23],[12,20,24,29])
diceStreakGamble([10,9,9,9,1,4],[10,9,9,9,1,4],[0,1,3,6,2,8],[1,2,2,1,0,1])
diceStreakGamble([2,45,56,6,4,10,34,20,3,4],[20,45,56,6,4,3,5,3,2,20],[3,4,20,20,21,30,33,35,35,36],[3,4,20,45,56,6,4,3,5,9])


