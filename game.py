class Game:
    SCENE_MENU = 'Menu'
    SCENE_GAME = 'Game'
    SCENE_CREDITS = 'Credits'
    SCENE_GAME_OVER = 'Game Over'

    def __init__(self, screen):
        self.scene = Game.SCENE_MENU
        self.screen = screen
        self.enabled = True

    def width_center(self, image):
        width = self.screen.get_rect().width
        return (width / 2) - (image.get_width() / 2)
