class Player:
    
    def __init__(self, name, points, rebounds, assists, blocks , steals, games_played ):
        self.name = name
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.blocks = blocks
        self.steals = steals
        self.games_played = games_played 

    
    def set_name(self,name):
        self.name = name

    def set_points(self, points):
        self.points = points

    def set_rebounds(self, rebounds):
        self.rebounds = rebounds

    def set_assists(self, assists):
        self.assists = assists

    def set_blocks(self, blocks):
        self.blocks = blocks

    def set_steals(self, steals):
        self.steals = steals

    def set_games_played(self, games_played):
        if games_played > 0:
            self.games_played = games_played 

    
    def get_name(self):
        return self.name

    def get_points(self):
        return self.points 

    def get_rebounds(self):
        return self.rebounds 

    def get_assists(self):
        return self.assists 

    def get_blocks(self):
        return self.blocks 

    def get_steals(self):
        return self.steals 

    def get_games_played(self):
        return self.games_played

    
    
