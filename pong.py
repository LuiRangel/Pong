import pygame
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from paddle import VPaddle
from paddle import HPaddleBottom
from paddle import HPaddleTop
from paddle import AIVPaddle
from paddle import AIHPaddleBottom
from paddle import AIHPaddleTop
from ball import Ball
from scoreboard import ScoreBoard
from game_stats import GameStats
from menu import Menu


def run_game():
    # initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pong")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    menu = Menu(screen, 'PONG', 'AI -- NO WALLS')

    # create a paddle
    paddles = Group()
    paddle1 = VPaddle(ai_settings, screen)
    paddle2 = HPaddleBottom(ai_settings, screen)
    paddle3 = HPaddleTop(ai_settings, screen)
    paddle4 = AIVPaddle(ai_settings, screen)
    paddle5 = AIHPaddleBottom(ai_settings, screen)
    paddle6 = AIHPaddleTop(ai_settings, screen)
    paddles.add(paddle1)
    paddles.add(paddle2)
    paddles.add(paddle3)

    # create ball
    ball = Ball(ai_settings, screen)

    # Begin the main loop
    while True:

        gf.check_events(ai_settings, stats, sb, menu, paddle1, paddle2, paddle3)
        if stats.game_active:
            for paddle in paddles:
                paddle.update(ai_settings)
            paddle4.update(ball)
            paddle5.update(ball)
            paddle6.update(ball)
            gf.move_ball(ai_settings, screen, sb, stats, paddles, paddle4, paddle5, paddle6, ball)

        gf.update_screen(menu, screen, ai_settings, sb, stats, paddles, paddle4, paddle5, paddle6, ball)


run_game()
