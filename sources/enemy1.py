import pygame
from player import Player

class Enemy1:
    
    def __init__(self, screen):
        self.screen = screen
        self.x = 500
        self.y = 125
        self.target_x = 400
        self.target_y = 100
        self.player = Player(self.screen)

    def draw(self):
        pygame.draw.circle(self. screen, "red", (self.x, self.y), 25)

    def move(self):
        if self.x > self.target_x:
            self.x -= 5
        else:
            self.x += 500

    def atack(self):
        if self.x == self.x(Player):
            pygame.quit