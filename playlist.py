# fav songs
afrobeats = {
    'last last': 'burna boy',
    'woman': 'rema',
    'osusu': 'famous pluto, jeriq',
    'for days': 'melvitto, AYOMIPO'
}


def playlist(playlist, file_name):
    with open('afrobeats.txt', 'w') as afro:
        afro.write("afrobeat playlist: \n")
        for song, artiste in afrobeats.items():
            afro.write(f"{song} by {artiste}\n")


playlist(afrobeats, 'afrobeats.txt')
