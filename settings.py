"""A class to store all settings for Alien Invasion"""
class Settings:
    """Initialize the game's static settings"""
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (3, 10, 50)
        
        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (8, 230, 0)
        self.bullets_allowed = 100

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #flee_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        #How quickly the game speeds up
        self.speedup_scale = 1.1
        
        #How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    #Initialize settings that change throughout the game
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 10
        self.alien_speed = 1.0
        
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        #Scoring
        self.alien_points = 50
    
    #Increase speed settings and alien point values
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        

        