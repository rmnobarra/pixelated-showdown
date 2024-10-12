import pygame

def draw_message(screen, message, width, height, y_offset=0):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text, text_rect)

def draw_progress_bar(screen, x, y, width, height, progress):
    border_color = (100, 100, 100)  # Gray
    bar_color = (255, 0, 0)  # Red
    background_color = (30, 30, 30)  # Dark Gray

    # Draw background
    pygame.draw.rect(screen, background_color, (x, y, width, height))

    # Draw progress
    progress_width = int(width * progress / 100)
    pygame.draw.rect(screen, bar_color, (x, y, progress_width, height))

    # Draw border
    pygame.draw.rect(screen, border_color, (x, y, width, height), 2)
