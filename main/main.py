from model.er_model import ERModel
from data_manager.csv_handler import CSVHandler

if __name__ == '__main__':
    option = input("Options:\n 1-Calculate ER with Basketball Reference Data\n>>")

    erModel = ERModel()
    csvHandler = CSVHandler()

    if (int(option)==1):
        player_list = csvHandler.loadBasketballReferenceCSV("FantasyBasketball2019SeasonPerGameStats.csv")
        scored_player_list = erModel.calculateERScores(player_list)
        csvHandler.writeScoredPlayerCSV(scored_player_list, "test_new_model")

