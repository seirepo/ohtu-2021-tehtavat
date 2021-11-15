class Player:
    def __init__(self, name, nationality, team,
                 games, assists, goals):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.games = games
        self.assists = assists
        self.goals = goals
    
    def __str__(self):
        return "\t" + self.name + " team " + self.team + " goals " + str(self.goals) + " assists " + str(self.assists)
