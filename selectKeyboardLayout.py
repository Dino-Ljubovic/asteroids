import pygame

from constants import (
    BUTTON_COLOR,
    BUTTON_HEIGHT,
    BUTTON_HOVER_COLOR,
    BUTTON_TEXT_COLOR,
    BUTTON_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class SelectKeyboardLayout(pygame.sprite.Sprite):
    options = ["Normal", "WTF?"]

    button1_rect = pygame.Rect(
        (
            SCREEN_WIDTH // 2 - BUTTON_WIDTH - 10,
            SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2,
        ),
        (BUTTON_WIDTH, BUTTON_HEIGHT),
    )
    button2_rect = pygame.Rect(
        (SCREEN_WIDTH // 2 + 10, SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2),
        (BUTTON_WIDTH, BUTTON_HEIGHT),
    )

    def __init__(self, x, y):
        print("initializing select keyboard layout")
        pygame.sprite.Sprite.__init__(self, self.containers)
        if SelectKeyboardLayout.containers:
            for container in SelectKeyboardLayout.containers:
                container.add(self)

    def draw_button(self, rect, text, hover, screen):
        font = pygame.font.Font(None, 36)
        color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
        pygame.draw.rect(screen, color, rect)
        text_surf = font.render(text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        button1_hover = self.button1_rect.collidepoint(mouse_pos)
        button2_hover = self.button2_rect.collidepoint(mouse_pos)

        self.draw_button(self.button1_rect, "wasd", button1_hover, screen)
        self.draw_button(self.button2_rect, "wtf??", button2_hover, screen)

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        # Button 1
        button1_hover = self.button1_rect.collidepoint(mouse_pos)
        if button1_hover and mouse_click[0]:
            print("Button 1 clicked")
        # Button 2
        button2_hover = self.button2_rect.collidepoint(mouse_pos)
        if button2_hover and mouse_click[0]:
            print("Button 2 clicked")
