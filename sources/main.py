import pygame
from player import Player

HEIGHT = 500
WEIGHT = 500

class Game:

    def __init_(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT, WEIGHT))
        self.back_surf = pygame.image.load('sources/back.jpg')
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen) 

    def game(self):
        self.draw()
        self.move()
        self.update()
        self.clock.tick(30)

    def draw(self):
        self.screen.blit(self.back_surf, (0, 0))
        self.player.draw()

    def move(self):
        for event in pygame.event.type():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        self.player.move(keys_pressed)

    def update(self):
        pygame.display.update()

game = Game()
game.game()