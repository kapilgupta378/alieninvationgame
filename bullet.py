import pygame
from pygame.sprite import Sprite

class Bullet(Sprint):
    """A class to mange bullets fired from the ship"""
    
    def __init__(self,ai_game):
        """Create a bullet object at the ship's curren position."""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = self.settings.bullet_color
    
        #Create a bullet rect at (0,0 and the set position
        self.rect = pygame.Rect(0,0, self.settiing.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
    
        #store the butte's position as a decimal value.
        self.y = float(self.rect.y)