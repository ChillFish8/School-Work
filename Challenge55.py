import pygame
from random import randint
import time

pygame.font.init()

clock = pygame.time.Clock()
BLACK = [000, 000, 15]
WHITE = [255, 255, 255]

Size = (512, 512)
screen = pygame.display.set_mode(Size)
pygame.mouse.set_visible(True)
pygame.display.set_caption("OX - Menace")
Font = pygame.font.SysFont('Comic Sans MS', 30)
Font2 = pygame.font.SysFont('Comic Sans MS', 120)

__Reset_Blank__ = [[False, False, False],
                   [False, False, False],
                   [False, False, False]]

class Board():
    class Cross:
        def __init__(self):
            self.board = [[False, False, False],
                          [False, False, False],
                          [False, False, False]]

        def cross_render_board(self):
            _X = 0
            _Y = 0
            for column in self.board:
                for row in column:
                    if row:
                        pygame.draw.line(screen, BLACK, (60 + _X, 160 + _Y), (160 + _X, 60 + _Y), 8)
                        pygame.draw.line(screen, BLACK, (60 + _X, 60 + _Y), (160 + _X, 160 + _Y), 8)
                        pygame.display.flip()
                        pygame.display.update()
                    _X += 145
                _X = 0
                _Y += 145

    class Naught:
        def __init__(self):
            self.board = [[False, False, False],
                          [False, False, False],
                          [False, False, False]]

        def naught_render_board(self):
            _X = 0
            _Y = 0
            for column in self.board:
                for row in column:
                    if row:
                        pygame.draw.circle(screen, BLACK, (108 + _X, 105 + _Y), 55, 4)
                        pygame.display.flip()
                        pygame.display.update()
                    _X += 145
                _X = 0
                _Y += 145

    def __init__(self):
        self.naught_board = self.Naught()
        self.cross_board = self.Cross()
        self.clock_tick = clock.tick(60)

    def render_board(self):
        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (175, 50), (175, 450), 5)
        pygame.draw.line(screen, BLACK, (325, 50), (325, 450), 5)
        pygame.draw.line(screen, BLACK, (50, 175), (450, 175), 5)
        pygame.draw.line(screen, BLACK, (50, 325), (450, 325), 5)
        pygame.display.flip()
        pygame.display.update()

    def run(self):
        global __Reset_Blank__
        self.cross_board.cross_render_board()
        self.naught_board.naught_render_board()

        time.sleep(0.5)
        for i in range(3):
            time.sleep(0.05)
            for x in range(3):
                time.sleep(0.05)
                self.cross_board.board[i][x] = True
                self.cross_board.cross_render_board()
        self.cross_board.board = __Reset_Blank__
        self.cross_board.cross_render_board()
        self.cross_board.cross_render_board()

        time.sleep(0.5)
        for i in range(3):
            time.sleep(0.05)
            for x in range(3):
                time.sleep(0.05)
                self.naught_board.board[i][x] = True
                self.naught_board.naught_render_board()
        self.naught_board.board = __Reset_Blank__
        self.naught_board.naught_render_board()
        self.naught_board.naught_render_board()


        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


def Run():

    Game = Board()
    Game.render_board()
    pygame.display.flip()
    Game.run()


Run()
