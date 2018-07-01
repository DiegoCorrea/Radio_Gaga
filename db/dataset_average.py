import os


def user_statistical():
    set_to_analyse = open(
        'db/set/playCount.csv',
        'r+'
        )
    songs = []
    users = []
    heard = []
    for line in set_to_analyse:
        lineSplit = line.split('\t')
        users.append(lineSplit[0])
        songs.append(lineSplit[1])
        heard.append(int(lineSplit[2]))
    songs_len = len(set(songs))
    users_len = len(set(users))
    heard_total = sum(heard)
    print('Songs: ' + str(songs_len))
    print('')
    print('Users: ' + str(users_len))
    print('+ Songs/Users ' + str(songs_len/users_len))
    print('')
    print('Heard: ' + str(heard_total))
    print('+ Heard/Users: ' + str(heard_total/users_len))
    print('+ Heard/Songs: ' + str(heard_total/songs_len))
