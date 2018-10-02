import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ball, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.vx = self.ai_settings.ball_vx
        self.vy = self.ai_settings.ball_vy
        self.sound = pygame.mixer.Sound('sounds/oof.wav')

        # load the ball's rect
        self.rect = pygame.Rect(self.screen_rect.centerx, self.screen_rect.centery, self.ai_settings.ball_width,
                                self.ai_settings.ball_height)

        # store the ball;s position as a decimal value (float)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
