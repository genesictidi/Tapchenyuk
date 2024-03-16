import pygame

class Player: 
    def __init__(self, screen): 
        self.screen = screen
        self.x = 250
        self.y = 250

    def draw(self): 
        pygame.draw.circle(self.screen, "black", (self.x, self.y), 25)

    def move(self, keys): 
        if keys[pygame.K_w]:
            self.y -= 10
        if keys[pygame.K_s]:
            self.y += 10
        if keys[pygame.K_a]:
            self.x -= 10
        if keys[pygame.K_d]:
            self.x += 10

    def update(self):
        pass