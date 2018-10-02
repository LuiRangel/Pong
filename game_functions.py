import pygame
import sys
from random import randint


def update_screen(menu, screen, ai_settings, sb, stats, paddles, paddle4, paddle5, paddle6, ball):
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # update each paddle in group
    for paddle in paddles:
        paddle.draw_paddle()
    paddle4.draw_paddle()
    paddle5.draw_paddle()
    paddle6.draw_paddle()
    draw_net(ai_settings, screen)
    # Don't understand why the ball wasn't being drawn without this here even tho move.ball draws the ball in
    pygame.draw.rect(screen, ai_settings.ball_color, ball.rect)

    if not stats.game_active:
        menu.draw_menu()
        pygame.mouse.set_visible(True)
        if ai_settings.winner:
            sb.draw_winner()

    sb.show_score()
    # Make the most recently drawn screen visible
    pygame.display.flip()


def move_ball(ai_settings, screen, sb, stats, paddles, paddle4, paddle5, paddle6, ball):
    ball.x = ball.x + ball.vx
    ball.y = ball.y + ball.vy

    # update the ball's position
    ball.rect.x = ball.x
    ball.rect.y = ball.y
    pygame.draw.rect(screen, ai_settings.ball_color, ball.rect)

    check_paddle_hit(screen, paddles, paddle4, paddle5, paddle6, ball)

    if check_wall_collision(screen, sb, stats, ball) == 1:
        center_ball(ai_settings, screen, ball)
        if stats.p_score == 15:
            sb.prep_p_winner()
            ai_settings.winner = True
            stats.reset_stats()
            stats.game_active = False

        elif stats.cp_score == 15:
            sb.prep_cp_winner()
            ai_settings.winner = True
            stats.reset_stats()
            stats.game_active = False


def check_wall_collision(screen, sb, stats, ball):
    """"returns 1 if out of bounds then updates score"""

    screen_rect = screen.get_rect()
    if ball.rect.bottom > screen_rect.bottom and ball.rect.centerx > screen_rect.centerx:
        stats.p_score += 1
        sb.prep_score()
        return 1

    if ball.rect.top < screen_rect.top and ball.rect.centerx > screen_rect.centerx:
        stats.p_score += 1
        sb.prep_score()
        return 1

    if ball.rect.left < screen_rect.left and ball.rect.centerx < screen_rect.centerx:
        stats.cp_score += 1
        sb.prep_score()
        return 1

    if ball.rect.right > screen_rect.right and ball.rect.centerx < screen_rect.centerx:
        stats.cp_score += 1
        sb.prep_score()
        return 1


def check_events(ai_settings, stats, sb, menu, paddle1, paddle2, paddle3):
    # watch for keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle1, paddle2, paddle3)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle1, paddle2, paddle3)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, sb, menu, mouse_x, mouse_y)


def check_keydown_events(event, paddle1, paddle2, paddle3):
    """Responds to keydown events."""
    if event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_UP:
        paddle1.moving_up = True

    elif event.key == pygame.K_DOWN:
        paddle1.moving_down = True

    elif event.key == pygame.K_LEFT:
        paddle2.moving_left = True
        paddle3.moving_left = True

    elif event.key == pygame.K_RIGHT:
        paddle2.moving_right = True
        paddle3.moving_right = True


def check_keyup_events(event, paddle1, paddle2, paddle3):
    """Responds to keyup events."""
    if event.key == pygame.K_UP:
        paddle1.moving_up = False

    elif event.key == pygame.K_DOWN:
        paddle1.moving_down = False

    elif event.key == pygame.K_LEFT:
        paddle2.moving_left = False
        paddle3.moving_left = False

    elif event.key == pygame.K_RIGHT:
        paddle2.moving_right = False
        paddle3.moving_right = False


def check_play_button(ai_settings, stats, sb, menu, mouse_x, mouse_y):
    """Starts a new game when the player clicks play"""
    button_clicked = menu.play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Set winner to false
        ai_settings.winner = False
        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        # reset score images
        sb.prep_score()


def check_paddle_hit(screen, paddles, paddle4, paddle5, paddle6, ball):
    screen_rect = screen.get_rect()
    collisions = pygame.sprite.spritecollide(ball, paddles, False, False)

    if collisions:
        for paddle in collisions:
            if paddle.rect.centery - 20 == screen_rect.top or paddle.rect.centery + 20 == screen_rect.bottom:
                ball.sound.play()
                ball.vy = -ball.vy * 1.25

            elif paddle.rect.centerx - 20 == screen_rect.left or paddle.rect.centerx + 20 == screen_rect.right:
                ball.sound.play()
                ball.vx = -ball.vx * 1.25

    if pygame.sprite.collide_rect(paddle4, ball):
        ball.sound.play()
        ball.vx = -ball.vx * 1.25
    if pygame.sprite.collide_rect(paddle5, ball) or pygame.sprite.collide_rect(paddle6, ball):
        ball.sound.play()
        ball.vy = -ball.vy * 1.25


def center_ball(ai_settings, screen, ball):
    screen_rect = screen.get_rect()
    ball.x = screen_rect.centerx
    ball.y = screen_rect.centery
    rand = randint(1, 4)
    if rand == 1:
        ball.vx = -ai_settings.ball_vx
        ball.vy = ai_settings.ball_vy
    if rand == 2:
        ball.vx = ai_settings.ball_vx
        ball.vy = -ai_settings.ball_vy
    if rand == 3:
        ball.vx = -ai_settings.ball_vx
        ball.vy = -ai_settings.ball_vy
    if rand == 4:
        ball.vx = ai_settings.ball_vx
        ball.vy = ai_settings.ball_vy


def draw_net(ai_settings, screen):
    rect = pygame.Rect(0, 0, 1, ai_settings.screen_height)
    screen_rect = screen.get_rect()
    rect.centerx = screen_rect.centerx
    pygame.draw.rect(screen, (230, 230, 230), rect)
