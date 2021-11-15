import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(type(response[0]))

    players = []
    nationalities = set()

    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict['nationality'],
            player_dict['team'], player_dict['games'],
            player_dict['assists'], player_dict['goals']
        )
        nationalities.add(player_dict['nationality'])
        players.append(player)

    print("Oliot:")

    players_fin = filter(lambda x: x.nationality == "FIN", players)
    for player in sorted(list(players_fin), key=lambda x: x.goals + x.assists, reverse=True):
        print(player)

if __name__ == "__main__":
    main()
