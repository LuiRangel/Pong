import pygame.font


class ScoreBoard:

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information
        self.text_color = (3, 241, 17)
        self.font = pygame.font.SysFont(None, 48)

        # initialize
        self.p_score_image = False
        self.p_score_rect = False
        self.cp_score_image = False
        self.cp_score_rect = False
        self.win_score_image = False
        self.win_score_rect = False
        self.winner_font = False
        self.winner_image = False
        self.winner_image_rect = False

        # Prepare the initial score images.
        self.prep_score()
        self.prep_winning_score()

    def prep_score(self):

        p_score_str = int(self.stats.p_score)
        self.p_score_image = self.font.render(str(p_score_str), True, self.text_color, self.ai_settings.bg_color)

        # Display the player score to the left of net
        self.p_score_rect = self.p_score_image.get_rect()
        self.p_score_rect.right = self.screen_rect.centerx - 20
        self.p_score_rect.top = 40

        cp_score_str = self.stats.cp_score
        self.cp_score_image = self.font.render(str(cp_score_str), True, self.text_color, self.ai_settings.bg_color)

        # Display the computer score to the right of net
        self.cp_score_rect = self.cp_score_image.get_rect()
        self.cp_score_rect.left = self.screen_rect.centerx + 20
        self.cp_score_rect.top = 40

    def prep_winning_score(self):
        self.win_score_image = self.font.render('15', True, self.text_color, self.ai_settings.bg_color)
        self.win_score_rect = self.win_score_image.get_rect()
        self.win_score_rect.centerx = self.screen_rect.centerx
        self.win_score_rect.top = self.screen_rect.top

    def show_score(self):
        """Draw scores and ships to the screen"""
        self.screen.blit(self.p_score_image, self.p_score_rect)
        self.screen.blit(self.cp_score_image, self.cp_score_rect)
        self.screen.blit(self.win_score_image, self.win_score_rect)

    def prep_p_winner(self):
            self.winner_font = pygame.font.SysFont(None, 50)
            self.winner_image = self.winner_font.render('Player Wins!', True, self.text_color,
                                                        self.ai_settings.bg_color)
            self.winner_image_rect = self.winner_image.get_rect()
            self.winner_image_rect.center = self.screen_rect.center

    def prep_cp_winner(self):
            self.winner_font = pygame.font.SysFont(None, 50)
            self.winner_image = self.winner_font.render('AI Wins!', True, self.text_color, self.ai_settings.bg_color)
            self.winner_image_rect = self.winner_image.get_rect()
            self.winner_image_rect.centerx = self.screen_rect.centerx
            self.winner_image_rect.centery = self.screen_rect.centery

    def draw_winner(self):
            self.screen.blit(self.winner_image, self.winner_image_rect)
