#A class to store all settings for Alien Invasion
class Settings:
    
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (3, 10, 50)
        
        #Ship settings
        self.ship_speed = 10
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (8, 230, 0)
        self.bullets_allowed = 100

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #flee_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1