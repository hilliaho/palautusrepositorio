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

    def test_search_returns_player(self):
        player_semenko = Player("Semenko", "EDM", 4, 12)
        search_semenko = self.statistics.search("Semenko")
        self.assertAlmostEqual(search_semenko.goals, player_semenko.goals)

    def test_search_return_none_if_player_doesnt_exist(self):
        player_none = self.statistics.search("Samenko")
        self.assertAlmostEqual(player_none, None)

    def test_team_returns_list(self):
        edm_joukkue = self.statistics.team("EDM")
        joukkue_nimet = list(map(lambda pelaaja: pelaaja.name, edm_joukkue))
        self.assertAlmostEqual(joukkue_nimet[0], "Semenko")

    def test_top_returns_top_players(self):
        top_kolme_nimet = list(
            map(lambda pelaaja: pelaaja.name, self.statistics.top(2)))
        self.assertAlmostEqual(
            top_kolme_nimet, ['Gretzky', 'Lemieux', 'Yzerman'])

    def test_top_sort_by_goals(self):
        top_kolme_nimet = list(
            map(lambda pelaaja: pelaaja.name, self.statistics.top(2, 2)))
        print(top_kolme_nimet)
        self.assertAlmostEqual(
            top_kolme_nimet, ['Lemieux', 'Yzerman', 'Kurri'])

    def test_top_sort_by_assists(self):
        top_kolme_nimet = list(
            map(lambda pelaaja: pelaaja.name, self.statistics.top(2, 3)))
        print(top_kolme_nimet)
        self.assertAlmostEqual(
            top_kolme_nimet, ['Gretzky', 'Yzerman', 'Lemieux']
        )
