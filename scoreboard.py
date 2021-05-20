import pygame.font 


"""A class to report scoring information"""
class Scoreboard:
    #Initialize scorekeeping attributes
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        #Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Prepare the initial score image
        self.prep_score()