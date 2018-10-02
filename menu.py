import pygame.font


class Menu:

    def __init__(self, screen, title, sub_title):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and the properties of the title
        self.title_font = pygame.font.SysFont(None, 100)
        self.sub_title_font = pygame.font.SysFont(None, 50)
        self.title_color = (3, 241, 17)
        self.title = title
        self.sub_title = sub_title

        # Initialize title variables (font, rect, ect) (had to do it so i can get a green checkmark
        self.title_image = False
        self.title_image_rect = False
        self.sub_title_image = False
        self.sub_title_image_rect = False

        self.play_button = Button(screen, 'PLAY')
        self.prep_title(self.title, self.sub_title)

    def prep_title(self, title, sub_title):
        # Draw title
        self.title_image = self.title_font.render(title, True, self.title_color, None)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.centery - (self.screen_rect.centery / 2)

        # Draw sub title
        self.sub_title_image = self.sub_title_font.render(sub_title, True, self.title_color, None)
        self.sub_title_image_rect = self.sub_title_image.get_rect()
        self.sub_title_image_rect.centerx = self.screen_rect.centerx
        self.sub_title_image_rect.centery = self.title_image_rect.bottom + 10

    def draw_menu(self):
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.sub_title_image, self.sub_title_image_rect)

        self.play_button.draw_button()


class Button:

    def __init__(self, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (3, 241, 17)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = self.screen_rect.centery + (self.screen_rect.centery / 2)
        self.rect.centerx = self.screen_rect.centerx

        # Initialize title variables (font, rect, ect) (had to do it so i can get a green checkmark
        self.msg_image = False
        self.msg_image_rect = False

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turns msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
