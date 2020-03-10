# \u200b

import os
import sys
import time
import pygame


def make_map():
    map_ = {"-": [f" {i}" for i in "ABCDEFGHIJ"]}
    for i in range(1, 11):
        map_[f"{i} "] = ["\u200b" for i in "ABCDEFGHIJ"]
    return map_


def get_keyboard_input():
    pass


class Board:
    def __init__(self):
        self.game_map = make_map()

    def clear_screen(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')
        return self

    def render(self):
        for row_key in self.game_map:
            print(row_key,
                  self.game_map[row_key][0],
                  self.game_map[row_key][1],
                  self.game_map[row_key][2],
                  self.game_map[row_key][3],
                  self.game_map[row_key][4],
                  self.game_map[row_key][5],
                  self.game_map[row_key][6],
                  self.game_map[row_key][7],
                  self.game_map[row_key][8],
                  self.game_map[row_key][9],)

    def add_marker(self, co_ords, hit=False, miss=False, ship=False):
        x = co_ords[0] if co_ords[0].isdigit() else [x for x in "ABCDEFGHIJ"].index(co_ords[0].upper())
        y = co_ords[1]
        if hit:
            self.game_map[f'{y} '][x] = "x"
        elif miss:
            self.game_map[f'{y} '][x] = "o"
        elif ship:
            self.game_map[f'{y} '][x] = "#"


class BattleShip(Board):
    def __init__(self):
        super().__init__()
        self.ships = {'5': [], '4': [], '3-1': [], '3-2': [], '2': []}

    def home_screen(self):
        for i in range(4):
            print(f'''Loading{"."*i}''')
            time.sleep(0.8)
            self.clear_screen()
        self.clear_screen()
        for i in range(10):
            print('######################################\n'
                  '##                                  ##\n'
                  '##         Game Starting in         ##\n'
                  f'##                {9 - i}                 ##\n'
                  '######################################\n')
            time.sleep(1)
            self.clear_screen()

    def start(self):
        self.home_screen()

        keys = pygame.key.get_pressed()


game = BattleShip()
game.start()