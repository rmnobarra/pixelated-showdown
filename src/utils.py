import pygame

def draw_message(screen, message, width, height, y_offset=0):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text, text_rect)

def draw_progress_bar(screen, x, y, width, height, progress):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width * (progress / 100), height))