POINTS_0 = "Love"
POINTS_1 = "Fifteen"
POINTS_2 = "Thirty"
POINTS_3 = "Forty"
POINTS_4_TIE = "Deuce"
ALL = "All"

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def point_won_by(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = self.score_all(self.m_score1)

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2
            score = self.score_advantage(minus_result)

        else:
            score1 = self.return_score(self.m_score1)
            score2 = self.return_score(self.m_score2)
            score = score1 + "-" + score2

        return score

    def return_score(self, score):
        result = ""
        if score == 0:
            result = POINTS_0
        elif score == 1:
            result = POINTS_1
        elif score == 2:
            result = POINTS_2
        elif score == 3:
            result = POINTS_3
        return result

    def score_all(self, score):
        result = self.return_score(score)
        if result == "":
            return POINTS_4_TIE
        return result + "-" + ALL

    def score_advantage(self, score_diff):
        adv = "Advantage "
        win = "Win for "

        if score_diff == 1:
            return adv + self.player1_name
        elif score_diff == -1:
            return adv + self.player2_name
        elif score_diff >= 2:
            return win + self.player1_name
        else:
            return win + self.player2_name