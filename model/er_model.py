from typing import List
from model.player import Player
from model.scored_player import ScoredPlayer

class ERModel:
    """
    Calculates the ER3/TER3 scores for a given Player(s)
    """

    # The following constants were precomputed using values from the 2018LeagueMatchCatAverages.xlsx spreadsheet in the data directory
    THREE_POINT_CONTR = 10.9203288
    REBOUND_CONTR = 2.638933456
    ASSIST_CONTR = 4.616546378
    STEAL_CONTR = 15.86632981
    BLOCK_CONTR = 23.25993266
    TURNOVER_CONTR = 7.79882592
    POINTS_CONTR = 1
    POINTS_AVERAGE_PER_MATCHUP = 575.6833333
    FIELD_GOAL_PERCENTAGE_CONTR = 0.46265
    FREE_THROW_PERCENTAGE_CONTR = 0.777633333

    PERCENTAGE_CONTRIBUTION_MULTIPLIER = 10000

    def calculateERScores(self, players: List[Player]) -> List[ScoredPlayer]:

        scored_player_list: List[ScoredPlayer] = []

        for player in players:
            ER = self.calculateERForPlayer(player)
            TER = self.calculateTERForPlayer(player, ER)
            scoredPlayer = ScoredPlayer(player = player, ER=ER, TER=TER)
            scored_player_list.append(scoredPlayer)

        return scored_player_list


    def calculateERForPlayer(self, player: Player):
        ER = self.THREE_POINT_CONTR * player.three_points_made + self.REBOUND_CONTR * player.total_rebounds + self.ASSIST_CONTR * player.assists + \
             self.STEAL_CONTR * player.steals + self.BLOCK_CONTR * player.blocks + self.POINTS_CONTR * player.points + \
             self.__calculatePercentageContribution(player.field_goals_percentage, player.field_goals_attempts, self.FIELD_GOAL_PERCENTAGE_CONTR) + \
             self.__calculatePercentageContribution(player.free_throws_percentage, player.free_throws_attempts, self.FREE_THROW_PERCENTAGE_CONTR)

        ER = '%.3f' % ER  # Truncate to 3 decimals

        return float(ER)

    def calculateTERForPlayer(self, player: Player, ER: float):
        TER = ER - self.TURNOVER_CONTR * player.turnovers
        TER = '%.3f' % TER # Truncate to 3 decimals
        return float(TER)

    def __calculatePercentageContribution(self, playerPercentageStat, playerAttempts, targetPercentage):
        """
        Calculates the contribution provided by a given percentage stat.
        :param playerPercentageStat: The player's percentage stat to compute the contribution from
        :param playerAttempts: The total times the player attempts towards the given percentage stat
        :param targetPercentage: The target percentage to compute the players contributiona against
        :return: The contribution of the player's stat to their total ER
        """
        try:
            percentageContribution = (((float(playerPercentageStat) - float(targetPercentage)) * float(playerAttempts))
                                      / self.POINTS_AVERAGE_PER_MATCHUP) * self.PERCENTAGE_CONTRIBUTION_MULTIPLIER
            return percentageContribution
        except Exception as e:
            print(str(e) + " ... defaulting to 0")
            return 0



