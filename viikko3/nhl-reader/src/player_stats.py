class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = self.filter_by_nationality(
            self.players, nationality)
        sorted_players = self.sort(filtered_players)
        return sorted_players

    def filter_by_nationality(self, players, nationality):
        return filter(lambda player: player.nationality == nationality, players)

    def sort(self, players):
        return sorted(players, reverse=True, key=self.sort_by_points)

    def sort_by_points(self, player):
        return player.points
