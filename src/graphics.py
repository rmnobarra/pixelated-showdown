import pygame

class Graphics:
    ARROW_KEYS = [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]

    def __init__(self, screen, width, height):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.load_images()
        self.create_background()

    def load_images(self):
        self.arrow_images = {
            pygame.K_LEFT: self.create_arrow_image("left"),
            pygame.K_UP: self.create_arrow_image("up"),
            pygame.K_RIGHT: self.create_arrow_image("right"),
            pygame.K_DOWN: self.create_arrow_image("down")
        }
        
        self.player_images = {
            "normal": self.create_player_image(),
            "shoot": self.create_player_shoot_image(),
            "win": self.create_player_win_image(),
            "hit": self.create_player_hit_image()
        }
        
        self.computer_images = {
            "normal": self.create_computer_image(),
            "shoot": self.create_computer_shoot_image(),
            "win": self.create_computer_win_image(),
            "hit": self.create_computer_hit_image()
        }

    def create_arrow_image(self, direction):
        size = 30
        image = pygame.Surface((size, size), pygame.SRCALPHA)
        color = (255, 255, 255)  # White color
        if direction == "left":
            pygame.draw.polygon(image, color, [(size, 0), (0, size//2), (size, size)])
        elif direction == "up":
            pygame.draw.polygon(image, color, [(0, size), (size//2, 0), (size, size)])
        elif direction == "right":
            pygame.draw.polygon(image, color, [(0, 0), (size, size//2), (0, size)])
        elif direction == "down":
            pygame.draw.polygon(image, color, [(0, 0), (size, 0), (size//2, size)])
        return image

    def create_pixel_art(self, width, height, color, pixels):
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pixel_size = min(width // len(pixels[0]), height // len(pixels))
        for y, row in enumerate(pixels):
            for x, pixel in enumerate(row):
                if pixel:
                    pygame.draw.rect(surface, color, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))
        return surface

    def create_player_image(self):
        pixels = [
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,1,0,0,1,0,0],
            [0,1,1,0,0,1,1,0],
            [1,1,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0]
        ]
        return self.create_pixel_art(50, 50, (0, 0, 0), pixels)

    def create_player_shoot_image(self):
        pixels = [
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,1,1,1,1],
            [0,0,0,1,1,0,0,1],
            [0,0,1,0,0,1,0,0],
            [0,1,1,0,0,1,1,0],
            [1,1,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0]
        ]
        return self.create_pixel_art(50, 50, (0, 0, 0), pixels)

    def create_player_win_image(self):
        pixels = [
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,1,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,0,0],
            [0,1,1,0,0,1,1,0],
            [1,1,0,0,0,0,1,1],
            [1,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0]
        ]
        return self.create_pixel_art(50, 50, (0, 0, 0), pixels)

    def create_player_hit_image(self):
        pixels = [
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,0,0],
            [0,1,0,0,0,0,1,0],
            [1,0,1,0,0,1,0,1],
            [0,0,1,0,0,1,0,0],
            [0,0,1,0,0,1,0,0]
        ]
        return self.create_pixel_art(50, 50, (0, 0, 0), pixels)

    def create_computer_image(self):
        pixels = [
            [0,1,1,1,1,1,0,0],
            [1,1,1,1,1,1,0,0],
            [1,0,1,1,1,0,0,0],
            [1,1,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,0],
            [0,0,1,1,1,0,0,1],
            [0,0,1,1,1,0,0,0],
            [0,0,1,0,1,0,0,0],
        ]
        return self.create_pixel_art(50, 50, (0, 0, 0), pixels)

    def create_computer_shoot_image(self):
        pixels = [
            [0,1,1,1,1,1,0,0],
            [1,1,1,1,1,1,0,0],
            [1,0,1,1,1,0,0,0],
            [1,1,1,1,1,1,1,1],
            [0,1,1,1,1,1,1,1],
            [0,0,1,1,1,0,0,1],
            [0,0,1,1,1,0,0,0],
            [0,0,1,0,1,0,0,0],
        ]
        return self.create_pixel_art(50, 50, (0, 0, 0), pixels)

    def create_computer_win_image(self):
        pixels = [
            [0,1,1,1,1,1,0,0],
            [1,1,1,1,1,1,0,0],
            [1,0,1,1,1,0,1,0],
            [1,1,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,0],
            [0,0,1,1,1,0,0,1],
            [0,1,1,0,1,1,0,0],
            [1,0,1,0,1,0,1,0],
        ]
        return self.create_pixel_art(50, 50, (0, 0, 0), pixels)

    def create_computer_hit_image(self):
        pixels = [
            [0,1,1,1,1,1,0,0],
            [1,1,1,1,1,1,0,0],
            [1,0,1,1,1,0,0,0],
            [1,1,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,0],
            [0,0,1,1,1,0,0,1],
            [0,1,0,1,0,1,0,0],
            [1,0,0,1,0,0,1,0],
        ]
        return self.create_pixel_art(50, 50, (0, 0, 0), pixels)

    def create_background(self):
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.background.fill((135, 206, 235))  # Sky blue
        pygame.draw.rect(self.background, (139, 69, 19), (0, self.HEIGHT - 100, self.WIDTH, 100))  # Ground

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def draw_arrow_combination(self, combination):
        for i, key in enumerate(combination):
            image = self.arrow_images.get(key)
            if image:
                self.screen.blit(image, (self.WIDTH - 250 + i * 35, 20))

    def get_player_image(self, state):
        return self.player_images.get(state, self.player_images["normal"])

    def get_computer_image(self, state):
        return self.computer_images.get(state, self.computer_images["normal"])