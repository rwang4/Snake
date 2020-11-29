import random
import pygame
import time


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


class Game:
    def __init__(self):
        surface
        bg_color = black
        time = 0
        close_clicked
        continue_game
        exposed_tiles = 0
        first_compare_tile = None
        images_list = []
        for i in range(1, 9):
            images_list.append(i)
        images_list *= 2
        random.shuffle(images_list)
        # image object
        pygame.image.load("images/image1.bmp")

        board = []
        for r in range(0, 4):
            row = []
            for c in range(0, 4):
                row.append(Tile(x, y, width, height, image, surface))
            board.append(row)

    def play(self):
        while not self.close_clicked:
            self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
        # time.sleep(0.01)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handlemousebuttonup(event.pos)

    def handlemousebuttonup(self, pos):
        tile = self.get_click_tile(pos)
        if tile is not None:
            tile.expose = True
            if first_compare_tile is None:
                first_compare_tile = tile
            elif first_compare_tile is not None and first_compare_tile.image == tile.image:
                first_compare_tile = None
                exposed_tiles += 2
            else:
                tile.draw()
                pygame.display.update()
                time.sleep(1)
                tile.expose = False
                first_compare_tile.expose = False
                first_compare_tile = None

    def draw(self):
        for r in board:
            for tile in r:
                draw Tile
        draw time
        update screen

    def draw_time(self):
        draw str(time)

    def get_click_tile(self, pos):
        for row in board:
            for tile in row:
                if tile.check_pos(pos):
                    return tile
        return None

    def update(self):
        # update time
        time = pygame.time.get_ticks()//1000

    def decide_continue(self):
        if exposed_tiles is 16:
            continue_game = False


class Tile:

    def __init__(self):
        position = (x, y)
        size = (width, height)
        surface
        boarder_width
        image
        hidden_image = pygame.image.load("images/image0.bmp")
        expose = False
        rect = pygame.Rect(postion, size)
    expose = True

    def draw(self):
        expose is True:
            draw rectangle(pygame.draw.rect)
            draw image(self.surface.blit)
        expose is False:
            draw rectangle(pygame.draw.rect)
            draw hidden_image(self.surface.blit)

    def check_pos(self, pos):
        if rect.collidepoint(pos) and expose is False:
            return True
        else:
            return False
