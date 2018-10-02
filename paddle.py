from pygame.sprite import Sprite
import pygame


class PaddleBase(Sprite):

    def __init__(self, ai_settings, screen):
        super(PaddleBase, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Create paddle
        self.rect = pygame.Rect(0, 0, ai_settings.paddle_width, ai_settings.paddle_height)
        self.color = ai_settings.paddle_color

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self, ai_settings):
        """Update the paddles position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= ai_settings.paddle_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += ai_settings.paddle_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= ai_settings.paddle_speed_factor

        if self.moving_right and self.rect.right < self.screen_rect.centerx:
            self.rect.centerx += ai_settings.paddle_speed_factor


class VPaddle(PaddleBase):

    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)

        # setup position of vertical paddle
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = 20
        # store decimal value for the paddle's center
        self.center = float(self.rect.centery)


class HPaddleTop(PaddleBase):

    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)

        # setup position of horizontal paddle
        self.rect.centery = self.screen_rect.top + 20
        self.rect.centerx = (self.screen_rect.centerx / 2)

        # store decimal value for the paddle's center
        self.center = float(self.rect.centery)
        self.rect.inflate_ip(90, -90)


class HPaddleBottom(PaddleBase):

    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)

        # setup position of horizontal paddle
        self.rect.centery = self.screen_rect.bottom - 20
        self.rect.centerx = (self.screen_rect.centerx / 2)

        # store decimal value for the paddle's center
        self.center = float(self.rect.centery)
        self.rect.inflate_ip(90, -90)
        # self.rect = pygame.transform.rotate()


class AIVPaddle(PaddleBase):

    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)

        self.rect.centerx = self.screen_rect.right - 20
        self.rect.centery = self.screen_rect.centery

    def update(self, ball):

        if self.rect.centery > ball.rect.y + 50 and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.ai_settings.paddle_speed_factor

        elif self.rect.centery < ball.rect.y - 50 and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.paddle_speed_factor
            
        super().update(ball)


class AIHPaddleBottom(PaddleBase):

    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)

        # setup position of horizontal paddle
        self.rect.centery = self.screen_rect.bottom - 20
        self.rect.centerx = self.screen_rect.centerx + (self.screen_rect.centerx / 2)
        # store decimal value for the paddle's center
        self.center = float(self.rect.centerx)
        self.rect.inflate_ip(90, -90)

        self.rect_cpy = self.rect.copy()
        # setup position of horizontal paddle
        self.rect_cpy.centery = self.screen_rect.top + 20
        self.rect_cpy.centerx = self.screen_rect.centerx + (self.screen_rect.centerx / 2)
        # store decimal value for the paddle's center
        self.center = float(self.rect.centerx)
        # self.rect_cpy.inflate_ip(90, -90)

    def update(self, ball):

        if self.rect.x > ball.rect.x + 50 and self.rect.left > self.screen_rect.centerx:
            self.rect.centerx -= self.ai_settings.paddle_speed_factor
            # self.rect_cpy.centerx -= self.ai_settings.paddle_speed_factor

        elif self.rect.x < ball.rect.x - 50 and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.paddle_speed_factor
            # self.rect_cpy.centerx += self.ai_settings.paddle_speed_factor

        super().update(ball)


class AIHPaddleTop(PaddleBase):

    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)

        # setup position of horizontal paddle
        self.rect.centery = self.screen_rect.top + 20
        self.rect.centerx = self.screen_rect.centerx + (self.screen_rect.centerx / 2)
        # store decimal value for the paddle's center
        self.center = float(self.rect.centerx)
        self.rect.inflate_ip(90, -90)

    def update(self, ball):

        if self.rect.x > ball.rect.x + 50 and self.rect.left > self.screen_rect.centerx:
            self.rect.centerx -= self.ai_settings.paddle_speed_factor
            # self.rect_cpy.centerx -= self.ai_settings.paddle_speed_factor

        elif self.rect.x < ball.rect.x - 50 and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.paddle_speed_factor
            # self.rect_cpy.centerx += self.ai_settings.paddle_speed_factor

        super().update(ball)
