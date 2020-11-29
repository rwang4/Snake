# Pre-Poke Framework
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to inlclude additional modules that are part of
# the Python Standard Library; no other modules are allowed

import pygame
import time
import random

# User-defined functions


def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption(
        'Memory')
    # get the display surface
    w_surface = pygame.display.get_surface()
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')
        self.time = 0
        self.pause_time = 0.01
        self.close_clicked = False
        self.continue_game = True
        self.images = []
        self.board = []
        self.exposedTiles = 0
        self.active = None

    def init_image(self):
        for i in range(1, 9):
            self.images.append(pygame.image.load("images/image"+str(i)+".bmp"))
        self.images *= 2
        random.shuffle(self.images)

    def create_board(self):
        for r in range(0, 4):
            row = []
            for c in range(0, 4):
                image = self.images[r*4 + c]
                width = image.get_width()
                height = image.get_height()
                x = width * c
                y = height * r
                tile = Tile(x, y, width, height, image, self.surface)
                row.append(tile)
            self.board.append(row)

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.
        self.init_image()
        self.create_board()
        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            # run at most with FPS Frames Per Second
            time.sleep(self.pause_time)

    def handle_events(self):

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handleMouseUp(event.pos)

    def handleMouseUp(self, pos):
        tile = self.get_tile(pos)
        if tile is not None and tile is not self.active:
            tile.expose = True
            if self.active is None:
                self.active = tile
            elif tile.image == self.active.image:
                self.active = None
                self.exposedTiles += 2
            else:
                tile.draw()
                pygame.display.update()
                time.sleep(0.5)
                tile.expose = False
                self.active.expose = False
                self.active = None

    def get_tile(self, pos):
        for r in self.board:
            for tile in r:
                if tile.check_pos(pos):
                    return tile
        return None

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        self.surface.fill(self.bg_color)  # clear the display surface first
        for r in range(0, 4):
            for c in range(0, 4):
                self.board[r][c].draw()
        self.draw_time()
        pygame.display.update()  # make the updated surface appear on the display

    def draw_time(self):
        time = str(self.time)
        bg_color = pygame.Color('white')
        text_font = pygame.font.SysFont('Comic Sans MS', 60)
        text_image = text_font.render(
            time, False, bg_color)
        self.surface.blit(
            text_image, (self.surface.get_width()-text_image.get_width(), 0))

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update
        self.time = pygame.time.get_ticks() // 1000

    def decide_continue(self):
        if self.exposedTiles == 16:
            self.continue_game = False


class Tile:
    # An object in this class represents a Dot that moves
    def __init__(self, x, y, width, height, image, surface):

        self.position = (x, y)
        self.size = (width, height)
        self.image = image
        self.surface = surface
        self.hidden_image = pygame.image.load("images/image0.bmp")
        self.boarder_width = 3
        self.expose = False
        self.rect = pygame.Rect(self.position, self.size)

    def show(self):
        pass

    def draw(self):
        if self.expose:
            pygame.draw.rect(self.surface, pygame.Color(
                "black"), self.rect, self.boarder_width)
            self.surface.blit(self.image, self.position)

        else:
            pygame.draw.rect(self.surface, pygame.Color(
                "black"), self.rect, self.boarder_width)
            self.surface.blit(self.hidden_image, self.position)

    def check_pos(self, pos):
        if not self.expose and self.rect.collidepoint(pos):
            return True
        else:
            return False


main()
