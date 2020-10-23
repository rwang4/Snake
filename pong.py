# Pre-Poke The Dots Version Five
# we are learning how to do the following things:
#
# Re-approach what we have written so far, with the goal of using a class to define the
# attributes and behaviors of a Game to be used in Poke the Dots.
#
# Some of the source code contained in this program is not original. It was borrowed from
# a tutorial found on pygame's website. Specifically, we used portions of this tutorial
# to respond to QUIT events and close the PyGame grapical window, to create a
# game window, and to understand how to use the flip() function to render graphics.
# https://www.pygame.org/docs/tut/PygameIntro.html
import pygame


def main():
    # initialize pygame -- this is required for rendering fonts
    pygame.init()

    # create the window and set its size to 500 width and 400 height
    size = (500, 400)
    screen = pygame.display.set_mode(size)

    # set the title of the window
    pygame.display.set_caption("Pong")

    game = Game(screen)
    game.play()


class Game:
    # the types of attributes that a game might have
    # --- general to all games
    # screen objects are being drawn to
    # background color
    # game clock
    # FPS limit
    # is the game over? (continue_game)
    # ---specific to poke the dots:
    # big dot
    # small dot
    # maximum frames
    # current frames
    def __init__(self, game_screen):
        # --- attributes that are general to all games
        self.screen = game_screen
        self.bg_color = pygame.Color('black')
        self.game_clock = pygame.time.Clock()
        self.FPS = 30
        self.continue_game = True
        self.close_clicked = False
        self.score1 = 0
        self.score2 = 0

        # --- attributes that are specific to Poke The Dots
        # game objects that are specific to poke the dots

        dot_color = pygame.Color('red')
        dot_pos = [300, 150]
        dot_velocity = [10, 4]
        dot_radius = 7
        self.dot = Dot(dot_color, dot_radius, dot_pos,
                       dot_velocity, self.screen)
        paddle_color = pygame.Color('white')
        paddle_size = (10, 70)
        p1_pos = (100, 150)
        p2_pos = (400, 150)
        paddle_velocity = [0, 0]

        self.p1 = Paddle(paddle_color, pygame.Rect(
            p1_pos, paddle_size), paddle_velocity, self.screen)
        self.p2 = Paddle(paddle_color, pygame.Rect(
            p2_pos, paddle_size), paddle_velocity, self.screen)

    def play(self):
        # Play the game until the player presses the close box.
        while not self.close_clicked:
            self.handle_events()
            self.draw()

            # look at game over conditions
            # if those conditions are not met:
            #   update the game state
            #   check if game over conditions are now met
            if self.continue_game:
                self.update()
                self.decide_continue()

            self.game_clock.tick(self.FPS)

    def handle_events(self):
        # Checks for new events generated by user input, and then change our
        # game state appropriately.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def draw(self):
        # draws all game objects to screen

        # clear our screen before we draw game objects
        self.screen.fill(self.bg_color)

        self.p1.draw()
        self.p2.draw()

        # draw our dot to screen
        self.dot.draw()

        # render all drawn objects to the screen
        pygame.display.flip()

    def update(self):
        # Update all of our game's objects
        self.check_bounce()
        self.check_collision()
        self.dot.move()

    def check_bounce(self):
        if (self.dot.center[0]+self.dot.radius > 500):
            self.dot.velocity[0] = -self.dot.velocity[0]
            self.score1 += 1
        elif (self.dot.center[0]-self.dot.radius < 0):
            self.dot.velocity[0] = -self.dot.velocity[0]
            self.score2 += 1
        elif (self.dot.center[1]+self.dot.radius > 400 or self.dot.center[1]-self.dot.radius < 0):
            self.dot.velocity[1] = -self.dot.velocity[1]

    def check_collision(self):
        if(self.dot.velocity[0] < 0 and self.p1.rect.collidepoint(self.dot.center)):
            self.dot.velocity[0] = - self.dot.velocity[0]
        elif(self.dot.velocity[0] > 0 and self.p2.rect.collidepoint(self.dot.center)):
            self.dot.velocity[0] = - self.dot.velocity[0]

    def decide_continue(self):
        # Check and remember if the game should continue
        if (self.score1 == 11):
            print("Player 1 win")
            self.continue_game = False
        elif (self.score2 == 11):
            print("Player 2 win")
            self.continue_game = False


class Dot:
    # represents a single 'dot' in Poke the Dots
    def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, screen):
        self.color = dot_color
        self.radius = dot_radius
        self.center = dot_center
        self.velocity = dot_velocity
        self.screen = screen

    def move(self):
        # Change the location of the Dot by adding the corresponding
        # speed values ot hte dot's x and y coordinates of its center.
        for index in range(0, 2):
            self.center[index] = self.center[index] + self.velocity[index]

    def draw(self):
        # Draw the dot onto the game's window
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)


class Paddle:

    def __init__(self, color, rect, velocity, screen):
        self.color = color
        self.rect = rect
        self.velocity = velocity
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move():
        pass


main()
