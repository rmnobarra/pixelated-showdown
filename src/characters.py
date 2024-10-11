import pygame
from src.graphics import Graphics  # Add this import at the top of the file

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "normal"
        self.animation_timer = 0
        self.ANIMATION_DURATION = 30

    def update(self):
        if self.animation_timer > 0:
            self.animation_timer -= 1
            if self.animation_timer == 0:
                if self.state == "shoot":
                    self.state = "win"
                    self.animation_timer = self.ANIMATION_DURATION * 2
                elif self.state in ["hit", "win"]:
                    self.state = "normal"

    def set_state(self, state):
        self.state = state
        self.animation_timer = self.ANIMATION_DURATION

    def draw(self, screen):
        image = self.get_image()
        screen.blit(image, (self.x, self.y))

    def get_image(self):
        raise NotImplementedError

class Player(Character):
    def __init__(self, x, y, graphics):
        super().__init__(x, y)
        self.graphics = graphics
        self.image = self.graphics.get_player_image(self.state)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        self.image = self.graphics.get_player_image(self.state)
        screen.blit(self.image, (self.x, self.y))

    def get_image(self):
        return self.graphics.get_player_image(self.state)

class Computer(Character):
    def __init__(self, x, y, graphics):
        super().__init__(x, y)
        self.graphics = graphics
        self.image = self.graphics.get_computer_image(self.state)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        self.image = self.graphics.get_computer_image(self.state)
        screen.blit(self.image, (self.x, self.y))

    def get_image(self):
        return self.graphics.get_computer_image(self.state)