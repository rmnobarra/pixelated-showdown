import pygame
import os
import time
from src.sound import SoundManager

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
        self.sound_manager = SoundManager()

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
            self.screen.blit(self.images[self.current_slide], (image_x, image_y))
            self.draw_text(self.texts[self.current_slide], (255, 255, 255), 
                           10, image_y + self.image_size[1] + 20, self.width - 20)
        else:
            self.draw_title_screen()
        pygame.display.flip()

    def draw_text(self, text, color, x, y, max_width):
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
        self.sound_manager.play_sound('presentation_music')
        for _ in range(len(self.images) + 1):  # +1 for the title screen
            self.draw()
            pygame.display.flip()
            
            start_time = time.time()
            while time.time() - start_time < 5:  # Show each slide for 5 seconds
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.sound_manager.stop_music()
                        return False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.sound_manager.stop_music()
                            return False
                        if event.key == pygame.K_RETURN and self.current_slide == len(self.images):
                            self.sound_manager.stop_music()
                            return True
                pygame.time.wait(100)  # Small delay to prevent high CPU usage
            
            self.current_slide += 1
        
        # Wait for ENTER key on the title screen
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.sound_manager.stop_music()
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                    if event.key == pygame.K_ESCAPE:
                        self.sound_manager.stop_music()
                        return False
            pygame.time.wait(100)
        
        self.sound_manager.stop_music()
        return True
