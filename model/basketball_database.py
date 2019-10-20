import csv
import os.path
from values import constants
import logging

#Calculates ER from downloaded player data
class BasketballDatabase(object):

    def calculateBasketballReferenceER(self):
        currentPath = os.path.abspath(os.path.dirname(__file__))

        csv_r = csv.reader(open(currentPath + '\\..\\data\\FantasyBasketball2019SeasonPerGameStats.csv', "r", encoding="utf8"))
        csv_w = csv.writer(open(currentPath + '\\..\\data\\FantasyBasketball2019SeasonPerGameStatsUpdated.csv', 'w', newline='', encoding="utf8"))

        index = 0

        for row in csv_r:
            if (index == 0):
              # First row of input CSV is the header row
              csv_w.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                              row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18],
                              row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27],
                              row[28], row[29], "Owned", "ER3", "TER3"])
            else:
                ER = 0
                try:
                    ER = constants.THREE_POINT_CONTR * float(row[11]) + constants.REBOUND_CONTR * float(row[23]) + constants.ASSIST_CONTR * float(row[24]) + \
                          constants.STEAL_CONTR * float(row[25]) + constants.BLOCK_CONTR * float(row[26]) + constants.POINTS_CONTR * float(row[29]) + \
                          self.__calculatePercentageContribution(row[10], row[9], constants.FIELD_GOAL_PERCENTAGE_CONTR) + \
                          self.__calculatePercentageContribution(row[20], row[19], constants.FREE_THROW_PERCENTAGE_CONTR)
                except Exception as e:
                    print(str(e))
                    print(f"3P:{row[11]}, REB:{row[23]}, AST:{row[24]}, STL:{row[25]}, BLOCK:{row[26]}, POINTS:{row[29]}, FG%:{row[10]}, FGA:{row[9]}, FT%:{row[20]}, FTA:{row[19]}")


                TER = ER - constants.TURNOVER_CONTR * float(row[27])

                ER = '%.3f' % ER  # Truncate to 3 decimals
                TER = '%.3f' % TER

                csv_w.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21],
                                row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], 0, ER, TER])

            print(index)
            index = index + 1

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
                                      / constants.POINTS_AVERAGE_PER_MATCHUP) * constants.PERCENTAGE_CONTRIBUTION_MULTIPLIER
            return percentageContribution
        except Exception as e:
            print(str(e) + " ... defaulting to 0")
            return 0


if __name__ == '__main__':
    option = input("Options:\n 1-Calculate ER with Basketball Reference Data\n>>")
    basketballDB = BasketballDatabase()
    if (int(option)==1):
        basketballDB.calculateBasketballReferenceER()
