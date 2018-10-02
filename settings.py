class Settings:
    """A class to store all static settings"""

    def __init__(self):
        """Initialize the games static settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # paddle settings
        self.paddle_width = 10
        self.paddle_height = 100
        self.paddle_color = (230, 230, 230)

        # ball settings
        self.ball_width = 20
        self.ball_height = 20
        self.ball_color = (230, 230, 230)

        self.paddle_speed_factor = 1.5

        # ball velocity
        self.ball_vx = -0.5
        self.ball_vy = 0.5

        # winner flag
        self.winner = False
