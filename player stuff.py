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

positions = [player['position']
             for player in players]  # creates a list of all player positions
print(positions)
update_player = input('which player do you want to update? \n').strip().lower()
player_name = next(
    # selects the next item in an iterator
    (player for player in players if player['name'] == update_player), None)
# player_name = None
# for p in players:
#     if p['name'] == update_player:
#         player_name = p
#         break
if player_name == None:
    print("player not in catalog")
    quit()

new_yards = int(input("Enter yards gained "))
new_touchdowns = int(input("enter touchdowns scored "))
player_name['stats']['yards'] += new_yards
player_name['stats']['touchdowns'] += new_touchdowns
print(f"updated stats: {player_name['stats']}")
