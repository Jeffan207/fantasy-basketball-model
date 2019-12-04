import csv
from typing import Final
import os.path

from typing import List
from model.scored_player import ScoredPlayer
from model.player import Player


class CSVHandler:

    CURRENT_PATH: Final[str] = os.path.abspath(os.path.dirname(__file__))
    BASKETBALL_DATABASE_CSV_DIR: Final[str] = CURRENT_PATH + '\\..\\data\\basketball_database\\'
    FANTASY_PROS_CSV_DIR: Final[str] = CURRENT_PATH + '\\..\\data\\fantasy_pros\\'
    OUTPUT_DIR: Final[str] = CURRENT_PATH + '\\..\\data\\output\\'

    @classmethod
    def loadBasketballReferenceCSV(self, file_name) -> List[Player]:

        print("Loading: ", file_name)
        file_path = self.BASKETBALL_DATABASE_CSV_DIR + file_name

        csv_r = csv.reader(open(file_path, "r", encoding="utf8"))

        index = 0
        player_list = []

        for row in csv_r:
            if (index == 0):
                # Skip the header
                index = index + 1
                continue
            else:
                field_goal_per = 0
                free_throw_per = 0
                if (row[10] != ""):
                    field_goal_per = float(row[10])
                if (row[20] != ""):
                    free_throw_per = float(row[20])

                try:
                    nextPlayer = Player(player=row[1], position=row[2], team=row[4], games=row[5], field_goals_made=float(row[8]), field_goals_attempts=float(row[9]),
                                        field_goals_percentage=field_goal_per, free_throws_made=float(row[18]), free_throw_attempts=float(row[19]), free_throw_percentages=free_throw_per,
                                        three_points_made=float(row[11]), total_rebounds=float(row[23]), assists=float(row[24]), steals=float(row[25]), blocks=float(row[26]),
                                        turnovers=float(row[27]), points=float(row[29]))
                    player_list.append(nextPlayer)
                except Exception as e:
                    # If a player is missing a stat that's not type checked, swallow the player for now.
                    print(str(e))
                    print(f"Player:{row[1]}, 3P:{row[11]}, REB:{row[23]}, AST:{row[24]}, STL:{row[25]}, BLOCK:{row[26]}, POINTS:{row[29]}, FG%:{row[10]}, FGA:{row[9]}, FT%:{row[20]}, FTA:{row[19]}")

            index = index + 1

        return player_list

    @classmethod
    def loadFantasyProsCSV(self, file_name) -> List[Player]:

        print("Loading: ", file_name)
        file_path = self.FANTASY_PROS_CSV_DIR + file_name

        csv_r = csv.reader(open(file_path, "r", encoding="utf8"))

        index = 0
        player_list = []

        for row in csv_r:
            if (index == 0):
                # Skip the header
                index = index + 1
                continue
            else:
                try:
                    # The Player class doesn't handle the 2PM stat, logic to compute fields is done outside
                    # Ideally, stat corrections should either both be made outside or inside the Player class
                    two_points_made = float(row[15])
                    three_points_made = float(row[10])
                    field_goals_made = two_points_made + three_points_made
                    field_goals_made = float('%.3f' % field_goals_made)

                    nextPlayer = Player(player=row[0], position=row[2], team=row[1], games=row[12], field_goals_made=field_goals_made, field_goals_attempts=None,
                                        field_goals_percentage=float(row[8]), free_throws_made=float(row[14]), free_throw_attempts=None, free_throw_percentages=float(row[9]),
                                        three_points_made=three_points_made, total_rebounds=float(row[4]), assists=float(row[5]), steals=float(row[7]), blocks=float(row[6]),
                                        turnovers=float(row[11]), points=float(row[3]))
                    player_list.append(nextPlayer)
                except Exception as e:
                    # If a player is missing a stat that's not type checked, swallow the player for now.
                    print(str(e))
                    print(f"Player:{row[0]}, 3P:{row[10]}, REB:{row[4]}, AST:{row[5]}, STL:{row[7]}, BLOCK:{row[6]}, POINTS:{row[3]}, FG%:{row[8]}, FT%:{row[9]}, FTM:{row[14]}")

            index = index + 1

        return player_list

    @classmethod
    def writeScoredPlayerCSV(self, player_list: List[ScoredPlayer], output_file_name):
        output_file_path = self.OUTPUT_DIR + output_file_name
        csv_w = csv.writer(open(output_file_path, 'w', newline='', encoding="utf8"))

        print("Writing player CSV to: ", output_file_path)

        # Write the header for the CSV
        csv_w.writerow(self.__playerCSVHeader())

        for scored_player in player_list:
            try:
                csv_w.writerow(scored_player.toList())
            except Exception as e:
                print(str(e))
                print("Error causing player: ", str(scored_player))
                exit(1)

        print("Finished writing players to CSV")

    @classmethod
    def __playerCSVHeader(self):
        return ["Player", "Pos", "Team", "Games", "FGM", "FGA", "FGPer", "FTM", "FTA", "FTPer", "Threes", "REB", "AS", "STL", "BLK", "TO", "PTS", "ER3", "TER3"]



