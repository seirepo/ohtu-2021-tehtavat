import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_top_scorers_palauttaa_top_scorerin(self):
        self.assertEqual(self.statistics.top_scorers(1)[0].name, "Gretzky")

    def test_search_palauttaa_oikean_pelaajan_kun_pelaaja_loytyy(self):
        result = self.statistics.search("Semenko")

        self.assertEqual(result.name, "Semenko")

    def test_search_palauttaa_Nonen_jos_pelaajaa_ei_loydy(self):
        result = self.statistics.search("asd")

        self.assertEqual(result, None)

    def test_team_palauttaa_oikeat_pelaajat(self):
        result = self.statistics.team("EDM")

        self.assertEqual(len(result), 3)

    def test_team_palauttaa_tyhjan_listan_jos_pelaajia_ei_ole(self):
        result = self.statistics.team("asd")

        self.assertEqual(len(result), 0)
