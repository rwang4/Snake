import pygame
import random


def main():
    bg = (255, 255, 255)
    (width, height) = (600, 400)
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption('Snake')
    screen.fill(bg)
    game = snake(screen, width, height)
    running = True
    while running:
        screen.fill(bg)
        game.play()
        pygame.display.flip()
        for event in pygame.event.get():
            game.keyPressed()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False


class snake():
    def __init__(self, screen, sw, sh):
        self.screen = screen
        self.sw = sw
        self.sh = sh
        init_w = self.sw/4
        init_h = self.sh/2
        self.rect = [
            [init_w, init_h, 11, 11],
            [init_w-11, init_h, 11, 11],
            [init_w-22, init_h, 11, 11],
            [init_w-33, init_h, 11, 11],
        ]
        self.velocity = (0, 0)
        self.circle = (random.randint(6, 594), random.randint(6, 394))
        self.score = 0

    def play(self):
        self.drawRects()
        self.drawCircle()
        self.move(self.velocity)
        if self.checkcollision():
            self.update()
        if self.checkknot():
            pygame.quit()

    def drawRects(self):
        for rect in self.rect:
            pygame.draw.rect(self.screen, [0, 0, 0], rect)

    def drawCircle(self):
        pygame.draw.circle(self.screen, [0, 0, 0], self.circle, 6)

    def move(self, velocity):
        next_rect = self.rect[0][:]
        self.rect[0][0] += velocity[0]
        self.rect[0][1] += velocity[1]
        if self.rect[0][0] > 700:
            self.rect[0][0] = 0
        elif self.rect[0][0] < 0:
            self.rect[0][0] = 700
        if self.rect[0][1] > 400:
            self.rect[0][1] = 0
        if self.rect[0][1] < 0:
            self.rect[0][1] = 400
        if velocity != (0, 0):
            for i in range(1, len(self.rect)):
                previous_rect = self.rect[i]
                self.rect[i] = next_rect
                next_rect = previous_rect[:]

    def keyPressed(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.velocity != (0, 11):
            self.velocity = (0, -11)
        elif key[pygame.K_s] and self.velocity != (0, -11):
            self.velocity = (0, 11)
        elif key[pygame.K_d] and self.velocity != (-11, 0):
            self.velocity = (11, 0)
        elif key[pygame.K_a] and self.velocity != (11, 0):
            self.velocity = (-11, 0)

    def update(self):
        last_rect = self.rect[-1][:]
        if self.velocity[0] < 0:
            last_rect[0] += 11
        elif self.velocity[0] > 0:
            last_rect[0] -= 11
        elif self.velocity[1] > 0:
            last_rect[1] -= 11
        elif self.velocity[1] < 0:
            last_rect[1] += 11
        self.rect.append(last_rect)
        self.circle = (random.randint(6, 594), random.randint(6, 394))
        self.score += 1

    def checkcollision(self):
        top_rect = self.rect[0]
        close_x = max(top_rect[0], min(self.circle[0], top_rect[0]+11))
        close_y = max(top_rect[1], min(self.circle[1], top_rect[1]+11))
        x = self.circle[0] - close_x
        y = self.circle[1] - close_y
        return (x*x + y*y) < (25)

    def checkknot(self):
        top_rect = self.rect[0]


        # if top_rect in self.rect:
        #     return True
        # if top_rect[0] > 600 or top_rect[0] < 0:
        #     return True
        # if top_rect[1] > 400 or top_rect[1] < 0:
        #     return True
main()
