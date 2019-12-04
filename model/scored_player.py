from model.player import Player


class ScoredPlayer:

    def __init__(self, player: Player, ER, TER):
        self.player = player
        self.ER = ER
        self.TER = TER

    def toList(self):
        scoredPlayerAttributes = self.player.toList()
        scoredPlayerAttributes.extend([self.ER, self.TER])
        return scoredPlayerAttributes

    def __str__(self):
        return str(self.toList())