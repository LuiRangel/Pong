class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state
        self.game_active = False
        self.p_score = 0
        self.cp_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.p_score = 0
        self.cp_score = 0
