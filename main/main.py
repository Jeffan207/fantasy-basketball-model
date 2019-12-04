from model.er_model import ERModel
from data_manager.csv_handler import CSVHandler

if __name__ == '__main__':
    option = input("Options:\n 1-Calculate ER with Basketball Reference Data\n 2-Calculate ER with Fantasy Pros Data\n>> ")

    erModel = ERModel()
    csvHandler = CSVHandler()

    if (int(option)==1):
        player_list = csvHandler.loadBasketballReferenceCSV("FantasyBasketball2019SeasonPerGameStats.csv")
        scored_player_list = erModel.calculateERScores(player_list)
        csvHandler.writeScoredPlayerCSV(scored_player_list, "test_new_model")
    if (int(option)==2):
        player_list = csvHandler.loadFantasyProsCSV("FantasyPros_Fantasy_Basketball_Overall_2019_Average_Stats_Last_15_Days.csv")
        scored_player_list = erModel.calculateERScores(player_list)
        csvHandler.writeScoredPlayerCSV(scored_player_list, "fantasy_pros_15_day_league")

