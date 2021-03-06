

"""Track statistics for Alien Invasion"""
class GameStats:
    #Initialize statistics
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        
        #Start Alien Invasion in an active state
        self.game_active = False
        
        #High score should not be reset
        self.high_score = 0
    
    #Initialize statistics that can change during the game
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    