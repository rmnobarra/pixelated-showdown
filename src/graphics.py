import pygame

class Graphics:
    ARROW_KEYS = [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]

    def __init__(self, screen, width, height):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.load_images()
        self.create_background()
        self.heart_image = self.create_heart_image()

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
        
        self.enemy_images = {
            "Little Bit": self.create_enemy_image("Little Bit"),
            "Brain Splitter": self.create_enemy_image("Brain Splitter"),
            "Slaughterhouse": self.create_enemy_image("Slaughterhouse"),
            "Boot": self.create_enemy_image("Boot"),
            "Few Locks": self.create_enemy_image("Few Locks"),
            "Dry Lagoon": self.create_enemy_image("Dry Lagoon"),
            "Little Chinese": self.create_enemy_image("Little Chinese"),
            "Dried Gut": self.create_enemy_image("Dried Gut")
        }

    def create_arrow_image(self, direction):
        size = 60  # Increased size
        image = pygame.Surface((size, size), pygame.SRCALPHA)
        color = (255, 255, 255)  # White color
        border_color = (100, 100, 100)  # Gray color for border
        
        # Draw the key border
        pygame.draw.rect(image, border_color, (0, 0, size, size))
        pygame.draw.rect(image, color, (2, 2, size-4, size-4))
        
        # Draw the arrow
        if direction == "left":
            arrow = [
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,1,1,0,0,0],
                [0,1,1,1,0,0,0],
                [1,1,1,1,1,1,1],
                [0,1,1,1,0,0,0],
                [0,0,1,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0]
            ]
        elif direction == "up":
            arrow = [
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,1,1,1,0,0],
                [0,1,1,1,1,1,0],
                [1,1,1,1,1,1,1],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0]
            ]
        elif direction == "right":
            arrow = [
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,1,0,0],
                [0,0,0,1,1,1,0],
                [1,1,1,1,1,1,1],
                [0,0,0,1,1,1,0],
                [0,0,0,1,1,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0]
            ]
        elif direction == "down":
            arrow = [
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [1,1,1,1,1,1,1],
                [0,1,1,1,1,1,0],
                [0,0,1,1,1,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0]
            ]
        
        pixel_size = 6
        for y, row in enumerate(arrow):
            for x, pixel in enumerate(row):
                if pixel:
                    pygame.draw.rect(image, (0, 0, 0), (x * pixel_size + 6, y * pixel_size + 6, pixel_size, pixel_size))
        
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
        arrow_size = 25  # Slightly smaller arrows
        spacing = 5
        total_width = len(combination) * (arrow_size + spacing) - spacing
        start_x = self.WIDTH - total_width - 10  # 10 pixels from the right edge
        start_y = 40  # Just below the enemy lives

        for i, key in enumerate(combination):
            image = self.arrow_images.get(key)
            if image:
                scaled_image = pygame.transform.scale(image, (arrow_size, arrow_size))
                self.screen.blit(scaled_image, (start_x + i * (arrow_size + spacing), start_y))

    def get_player_image(self, state):
        return self.player_images.get(state, self.player_images["normal"])

    def get_computer_image(self, state):
        return self.computer_images.get(state, self.computer_images["normal"])

    def create_heart_image(self):
        size = 20
        image = pygame.Surface((size, size), pygame.SRCALPHA)
        color = (255, 0, 0)  # Red color for heart
        
        heart = [
            [0,1,1,0,1,1,0],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            [0,1,1,1,1,1,0],
            [0,0,1,1,1,0,0],
            [0,0,0,1,0,0,0],
        ]
        
        pixel_size = 2
        for y, row in enumerate(heart):
            for x, pixel in enumerate(row):
                if pixel:
                    pygame.draw.rect(image, color, (x * pixel_size + 3, y * pixel_size + 4, pixel_size, pixel_size))
        
        return image

    def draw_player_lives(self, lives):
        for i in range(lives):
            self.screen.blit(self.heart_image, (10 + i * 25, 10))

    def draw_enemy_lives(self, lives):
        for i in range(lives):
            self.screen.blit(self.heart_image, (self.WIDTH - 30 - i * 25, 10))

    def create_enemy_image(self, enemy_name):
        # Create different pixel art for each enemy
        if enemy_name == "Little Bit":
            pixels = [
                [0,0,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,0],
                [1,0,1,0,0,1,0,1],
                [1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,0],
                [0,0,1,0,0,1,0,0],
                [0,1,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,1]
            ]
        elif enemy_name == "Brain Breaker":
            pixels = [
                [0,1,1,1,1,1,1,0],
                [1,1,0,1,1,0,1,1],
                [1,0,1,1,1,1,0,1],
                [1,1,1,0,0,1,1,1],
                [1,1,0,1,1,0,1,1],
                [0,1,1,1,1,1,1,0],
                [0,0,1,0,0,1,0,0],
                [0,1,0,0,0,0,1,0]
            ]
        # ... (create pixel art for other enemies)
        else:
            pixels = [
                [0,1,1,1,1,1,0,0],
                [1,1,1,1,1,1,1,0],
                [1,0,1,1,1,0,1,0],
                [1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,0],
                [0,0,1,1,1,0,1,0],
                [0,1,0,1,0,1,0,0],
                [1,0,0,1,0,0,1,0]
            ]
        return self.create_pixel_art(50, 50, (0, 0, 0), pixels)

    def get_enemy_image(self, enemy_name):
        return self.enemy_images.get(enemy_name, self.enemy_images["Little Bit"])