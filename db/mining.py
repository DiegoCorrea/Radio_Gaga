import os


def structure_Data_Users():
    userDict = {}
    directory = 'db/set/'
    status = 0
    if not os.path.exists(directory):
        os.makedirs(directory)
    for line in open(
        'db/oneMillionSongs/playCount.csv',
        'r+'
    ):
        status += 1
        if status == 1:
            continue
        if (status % 1000 == 0):
            print ("-> [", status, "]")
        lineSplit = line.split(',')
        if lineSplit[0] not in userDict:
            userDict.setdefault(lineSplit[0], {})
            userDict[lineSplit[0]][lineSplit[1]] = lineSplit[2]
        elif (lineSplit[1] in userDict[lineSplit[0]]):
            userDict[lineSplit[0]][lineSplit[1]] = lineSplit[2] + userDict[lineSplit[0]][lineSplit[1]]
        else:
            userDict[lineSplit[0]][lineSplit[1]] = lineSplit[2]
    return userDict


def selectUsers(userDict):
    songListID = []
    usersToSaveFile = open(
        'db/set/users.csv',
        'w+'
    )
    playCountToSaveFile = open(
        'db/set/playCount.csv',
        'w+'
    )
    usersToSaveFile.write('id\n')
    playCountToSaveFile.write('id,user_id,song_id,play_count\n')
    count = 0
    for user in userDict:
        if len(userDict[user]) > 50:
            usersToSaveFile.write(user + "\n")
            for song in userDict[user]:
                if song not in set(songListID):
                    songListID.append(song)
                playCountToSaveFile.write(
                    str(count)
                    + ','
                    + str(user)
                    + ','
                    + str(song)
                    + ','
                    + str(userDict[user][song])
                )
                count += 1
                if len(set(songListID)) >= 5000:
                    usersToSaveFile.close()
                    playCountToSaveFile.close()
                    return set(songListID)
    usersToSaveFile.close()
    playCountToSaveFile.close()
    return set(songListID)


def selectSongs(songListID):
    status = 0
    songsToSaveFile = open(
        'db/set/songs.csv',
        'w+'
    )
    songsToSaveFile.write('id,title\n')
    for line in open(
        'db/oneMillionSongs/songs.csv',
        'r+'
    ):
        status += 1
        if (status % 1000 == 0):
            print ("-> [", status, "]")
        lineSplit = line.split(',')
        if lineSplit[0] not in set(songListID):
            continue
        songsToSaveFile.write(lineSplit[0] + ',' + lineSplit[1] + '\n')
    songsToSaveFile.close()


def start():
    selectSongs(selectUsers(structure_Data_Users()))


##########
start()
