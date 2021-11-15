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
        return f"{self.nationality} \t {self.name:20} {self.team} {str(self.goals):2} + {str(self.assists):2} = {str(self.goals + self.assists)}"
        #return "\t" + self.name + " team " + self.team + str(self.goals) + " + " + str(self.assists)
