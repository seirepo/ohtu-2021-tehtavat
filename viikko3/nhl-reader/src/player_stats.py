from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered_players = filter(lambda x: x.nationality == nationality, players)
        return sorted(list(filtered_players), key=lambda x: x.goals + x.assists, reverse=True)