def matchPlayersAndTrainers(players, trainers):
    players.sort()
    trainers.sort()
    count = 0
    play = 0
    train = 0
    while play < len(players) and train < len(trainers) :
        if players[play] <= trainers[train]:
            count += 1
            play += 1
        train += 1
    return count 

players = [4,7,9]
trainers = [8,2,5,8]
print(matchPlayersAndTrainers(players, trainers))