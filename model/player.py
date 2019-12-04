

class Player:
    """The player class represents a single basketball player. Is used with the model to commute the players ER"""
    def __init__(self, player, position, team, games,  field_goals_made, field_goals_attempts, field_goals_percentage,
                 free_throws_made, free_throw_attempts, free_throw_percentages, three_points_made, total_rebounds, assists,
                 steals, blocks, turnovers, points):
        self.player = player
        self.position = position
        self.team = team
        self.games = games
        self.field_goals_made = field_goals_made
        self.field_goals_attempts = field_goals_attempts
        self.field_goals_percentage = field_goals_percentage
        self.free_throws_made = free_throws_made
        self.free_throws_attempts = free_throw_attempts
        self.free_throws_percentage = free_throw_percentages
        self.three_points_made = three_points_made
        self.total_rebounds = total_rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.points = points

        if (self.field_goals_attempts == None):
            self.field_goals_attempts = self.__calculateAttempts(self.field_goals_made, self.field_goals_percentage)

        if (self.free_throws_attempts == None):
            self.free_throws_attempts = self.__calculateAttempts(self.free_throws_made, self.free_throws_percentage)

    def __calculateAttempts(self, made, percentage):
        if (percentage < 0.0001):
            return 0.0
        attempts = float(made/percentage)
        attempts = '%.3f' % attempts
        return attempts

    def toList(self):
        return [self.player, self.position, self.team, self.games, self.field_goals_made, self.field_goals_attempts, self.field_goals_percentage,
                self.free_throws_made, self.free_throws_attempts, self.free_throws_percentage, self.three_points_made, self.total_rebounds, self.assists,
                self.steals, self.blocks, self.turnovers, self.points]

    def __str__(self):
        return str(self.toList())





