from PlayerStats import Player

class Stats:
    def __init__(self):

        self.players = {}

    def getPPG(self, player):
        # find the points per game avergae from one player
        return player.points / player.games_played
        
    
    def getRPG(self,player):
        # find the rebounds per game avergae from one player
        return player.rebounds / player.games_played
        
    
    def getAPG(self, player):
        # find the assists per game avergae from one player
        return player.assists / player.games_played
     
    
    def getBPG(self, player):
        # find the blocks per game avergae from one player
        return player.blocks / player.games_played
        
    

    def getSPG(self, player):
        # find the steals per game avergae from one player
        return player.steals / player.games_played
        
    
    def get_games_played(self,player):
        return player.games_played

    



