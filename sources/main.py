import pygame
from player import Player
from enemy1 import Enemy1

HEIGHT = 500
WEIGHT = 500

class Game:

    def game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT, WEIGHT))
        self.back_surf = pygame.image.load('sources/back.jpg')
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen) 
        self.enemy1 = Enemy1(self.screen)

    def game(self):
        while True:
            self.draw()
            self.move()
            self.update()
            self.clock.tick(30)

    def draw(self):
        self.screen.blit(self.back_surf, (WEIGHT,HEIGHT))
        self.player.draw()
        self.enemy1.draw()

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        self.player.move(keys_pressed)
        self.enemy1.move()

    def update(self):
        pygame.display.update()

game = Game()
game.game()