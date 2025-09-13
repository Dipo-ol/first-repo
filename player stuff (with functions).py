# player stuff
players = [
    {
        'name': 'patrick mahomes',
        'position': 'quarterback',
        'jersey_no': 15,
        'stats': {'yards': 3928, 'touchdowns': 26}
    },
    {
        'name': 'tyreck hill',
        'position': 'wide receiver',
        'jersey_no': 10,
        'stats': {'yards': 956, 'touchdowns': 6}
    },
    {
        'name': 'travis kelce',
        'position': 'tight end',
        'jersey_no': 87,
        'stats': {'yards': 823, 'touchdowns': 3}
    }
]


def player_selection():
    update_player = input(
        'which player do you want to update ?\n').strip().lower()
    player_name = next((player
                       for player in players if player['name'] == update_player), None)
    if player_name == None:
        print("player is not in catalog")
        quit()
    return player_name


player_select = player_selection()


def update_stats(player_name):
    new_yards = int(input("Enter yards gained "))
    new_touchdowns = int(input("enter touchdowns scored "))
    player_name['stats']['yards'] += new_yards
    player_name['stats']['touchdowns'] += new_touchdowns
    print(f"updated stats: {player_name['stats']}")


update_stats(player_select)
