import pygame
import os
import time

class Presentation:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 32)
        self.title_font = pygame.font.Font(None, 64)  # Larger font for the title
        self.image_size = (600, 400)
        self.text_height = 150
        self.images = self.load_images()
        self.texts = [
            "A long time ago, in the middle of nowhere, the peace of the people was quiet and peaceful. But, suddenly, everything changes.",
            "Humble folk suffered at the hands of outlaws. Robbery, murder, and countless other crimes plagued the daily lives of these poor people.",
            "One day, a gang of the most dangerous and ruthless men, known as the \"Dried Gut,\" attacked a farming village, killing the men and abducting the women and children.",
            "Amidst the chaos of these brutal assaults, one family was slaughtered—the family of a retired gunslinger.",
            "That day, the Dried Gut gang made a fatal mistake. The gunslinger vowed revenge—deadly revenge."
        ]
        self.current_slide = 0
        self.fade_alpha = 0
        self.fade_speed = 5

    def load_images(self):
        images = []
        for i in range(1, 6):
            image_path = os.path.join('assets', 'images', f'0{i}.png')
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, self.image_size)
            images.append(image)
        return images

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        if self.current_slide < len(self.images):
            image_x = (self.width - self.image_size[0]) // 2
            image_y = (self.height - self.image_size[1] - self.text_height) // 2
            
            # Draw the current image with fade effect
            image_with_alpha = self.images[self.current_slide].copy()
            image_with_alpha.set_alpha(self.fade_alpha)
            self.screen.blit(image_with_alpha, (image_x, image_y))
            
            # Draw text with fade effect
            self.draw_text(self.texts[self.current_slide], (255, 255, 255), 
                           10, image_y + self.image_size[1] + 20, self.width - 20, self.fade_alpha)
        else:
            self.draw_title_screen()
        pygame.display.flip()

    def draw_text(self, text, color, x, y, max_width, alpha):
        words = text.split()
        lines = []
        current_line = []
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_surface = self.font.render(test_line, True, color)
            if test_surface.get_width() <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))

        total_height = len(lines) * self.font.get_linesize()
        current_y = y + (self.text_height - total_height) // 2

        for line in lines:
            text_surface = self.font.render(line, True, color)
            text_surface.set_alpha(alpha)
            text_rect = text_surface.get_rect(center=(self.width // 2, current_y))
            self.screen.blit(text_surface, text_rect)
            current_y += self.font.get_linesize()

    def draw_title_screen(self):
        title_text = "The Pixelated Showdown"
        title_surface = self.title_font.render(title_text, True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(title_surface, title_rect)

        subtitle_text = "Press ENTER to start the game"
        subtitle_surface = self.font.render(subtitle_text, True, (255, 255, 255))
        subtitle_rect = subtitle_surface.get_rect(center=(self.width // 2, self.height // 2 + 50))
        self.screen.blit(subtitle_surface, subtitle_rect)

    def run(self):
        clock = pygame.time.Clock()
        for _ in range(len(self.images) + 1):  # +1 for the title screen
            self.fade_alpha = 0
            start_time = pygame.time.get_ticks()
            
            while self.fade_alpha < 255:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return False
                        if event.key == pygame.K_RETURN and self.current_slide == len(self.images):
                            return True
                
                self.fade_alpha = min(255, self.fade_alpha + self.fade_speed)
                self.draw()
                pygame.display.flip()
                clock.tick(60)
            
            # Keep the slide visible for a few seconds
            while pygame.time.get_ticks() - start_time < 5000:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return False
                        if event.key == pygame.K_RETURN and self.current_slide == len(self.images):
                            return True
                clock.tick(60)
            
            self.current_slide += 1
        
        # Wait for ENTER key on the title screen
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                    if event.key == pygame.K_ESCAPE:
                        return False
            clock.tick(60)
        
        return True
