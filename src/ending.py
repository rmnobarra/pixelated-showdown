import pygame
import sys
import os

class EndingScene:
    def __init__(self, screen, sound_manager):
        self.screen = screen
        self.sound_manager = sound_manager
        self.WIDTH, self.HEIGHT = screen.get_size()
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 72)
        self.image_size = (600, 400)
        self.text_height = 150
        self.fade_alpha = 0
        self.fade_speed = 5

    def load_images(self):
        images = []
        for i in range(6, 9):  # Ending images are 06.png, 07.png, 08.png
            image_path = os.path.join('assets', 'images', f'0{i}.png')
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, self.image_size)
            images.append(image)
        return images

    def show_ending(self):
        self.sound_manager.stop_music()  # Ensure all music is stopped
        self.sound_manager.play_sound('the_final_sunset')
        
        ending_images = self.load_images()
        
        ending_texts = [
            "After a bloody journey of retribution, the gunslinger finally fulfilled his promise, and the entire Dried Gut gang was defeated.",
            "At last, his family could rest in peace...",
            "and once more, his guns were laid to rest."
        ]
        
        clock = pygame.time.Clock()
        
        for image, text in zip(ending_images, ending_texts):
            self.fade_alpha = 0
            start_time = pygame.time.get_ticks()
            
            while self.fade_alpha < 255 or pygame.time.get_ticks() - start_time < 5000:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return "quit"
                
                self.screen.fill((0, 0, 0))  # Black background
                
                # Draw the current image with fade effect
                image_with_alpha = image.copy()
                image_with_alpha.set_alpha(self.fade_alpha)
                image_x = (self.WIDTH - self.image_size[0]) // 2
                image_y = (self.HEIGHT - self.image_size[1] - self.text_height) // 2
                self.screen.blit(image_with_alpha, (image_x, image_y))
                
                # Draw text with fade effect
                self.draw_text(text, (255, 255, 255), 
                               10, image_y + self.image_size[1] + 20, self.WIDTH - 20, self.fade_alpha)
                
                if self.fade_alpha < 255:
                    self.fade_alpha = min(255, self.fade_alpha + self.fade_speed)
                
                pygame.display.flip()
                clock.tick(60)
        
        return self.show_options()

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
            text_rect = text_surface.get_rect(center=(self.WIDTH // 2, current_y))
            self.screen.blit(text_surface, text_rect)
            current_y += self.font.get_linesize()

    def show_options(self):
        self.screen.fill((0, 0, 0))
        
        title_surface = self.title_font.render("Pixelated Showdown", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 - 100))
        self.screen.blit(title_surface, title_rect)
        
        text_surface = self.font.render("The end.", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(text_surface, text_rect)
        
        new_game_surface = self.font.render("Press N for New Game", True, (255, 255, 255))
        new_game_rect = new_game_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 100))
        self.screen.blit(new_game_surface, new_game_rect)
        
        quit_surface = self.font.render("Press Q to Quit", True, (255, 255, 255))
        quit_rect = quit_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 150))
        self.screen.blit(quit_surface, quit_rect)
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.sound_manager.stop_music()  # Stop music before quitting
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.sound_manager.stop_music()  # Stop music before new game
                        return "new_game"
                    elif event.key == pygame.K_q:
                        self.sound_manager.stop_music()  # Stop music before quitting
                        return "quit"
        
        self.sound_manager.stop_music()  # Ensure music is stopped if loop is exited
        return "quit"  # Default action if the loop is somehow exited
