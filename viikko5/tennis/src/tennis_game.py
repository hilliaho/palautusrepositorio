class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @property
    def get_name(self):
        return self.name

    @property
    def get_score(self):
        return self.score


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name, score=0)
        self.player2 = Player(player2_name, score=0)
        self.points = ["Love", "Fifteen", "Thirty", "Forty", "Deuce"]

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.score = self.player1.score + 1
        else:
            self.player2.score = self.player2.score + 1

    def get_score(self):
        if self.player1.score == self.player2.score:
            if self.player1.score >= 4:
                score = "Deuce"
            else:
                score = f"{self.points[self.player1.score]}-All"

        elif self.player1.score >= 4 or self.player2.score >= 4:

            if self.player1.score > self.player2.score:
                better_player = self.player1.name
            else:
                better_player = self.player2.name

            minus_result = self.player1.score - self. player2.score
            print(better_player)
            if minus_result == 1 or minus_result == -1:
                score = f"Advantage {better_player}"
            elif minus_result >= 2 or minus_result <= -2:
                score = f"Win for {better_player}"
        else:
            score = f"{self.points[self.player1.score]}-{self.points[self.player2.score]}"

        return score
