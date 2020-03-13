# \u200b

import os
import sys
import time
import itertools
import keyboard


def make_map():
    map_ = {"-": [f" {i}" for i in "ABCDEFGHIJ"]}
    for i in range(1, 11):
        map_[f"{i}"] = ["\u200b" for i in "ABCDEFGHIJ"]
    return map_


def get_keyboard_input():
    pass


class Board:
    def __init__(self):
        self.game_map = make_map()
        self.game_blank = make_map()

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
            self.game_map[f'{y}'][x] = " x"
        elif miss:
            self.game_map[f'{y}'][x] = " o"
        elif ship:
            self.game_map[f'{y}'][x] = " #"


class BattleShips(Board):
    def __init__(self):
        super().__init__()
        self.ships = []

    class Ship:
        def __init__(self, hp, co_ords):
            self.co_ords = co_ords
            self.hp = hp

    def home_screen(self):
        for i in range(4):
            print(f'''Loading{"."*i}''')
            time.sleep(0.8)
            self.clear_screen()
        self.clear_screen()
        choice = "_"
        while choice not in ['Y', 'N']:
            choice = input("Start Game? Y/N")
            choice = choice.upper()
        return choice == "Y"

    def place_ships(self):
        class ShipCreator:
            def __init__(self, size):
                self.positions = [{'hit': False, 'pos': ['ABCDEFGHIJ'[x], 1]} for x in range(size)]    # Default start
                self.destroyed = False

            def is_hit(self, co_ords):
                for index, pos_dict in enumerate(self.positions):
                    if co_ords == pos_dict['pos']:
                        self.positions[index]['hit'] = True
                        return True
                else:
                    return False

            def is_destroyed(self):
                amount_destroyed = 0
                for pos in self.positions:
                    if pos['hit']:
                        amount_destroyed += 1
                return amount_destroyed == len(self.positions)

            def move(self, x=0, y=0, rotate=False):
                LETTERS = 'ABCDEFGHIJ'
                new_co_ords = []
                if x:
                    for pos_dict in self.positions:
                        pos_dict['pos'][0] = LETTERS[LETTERS.index(pos_dict['pos'][0]) + x]
                        new_co_ords.append(pos_dict)
                elif y:
                    for pos_dict in self.positions:
                        pos_dict['pos'][1] = pos_dict['pos'][1] - y
                        new_co_ords.append(pos_dict)
                elif rotate:
                    for pos_dict in self.positions:
                        pos_dict['pos'][0] = LETTERS[LETTERS.index(pos_dict['pos'][0]) + x]
                        new_co_ords.append(pos_dict)
                print(new_co_ords)
                self.positions = new_co_ords

        for ship_size in [5, 4, 3, 3, 2]:
            self.ships.append(ShipCreator(ship_size))

        cycler = itertools.cycle(self.ships)
        ship = next(cycler)

        running_main = True
        while running_main:
            self.clear_screen()
            self.game_map = make_map()
            for co_ord in ship.positions:
                self.add_marker(co_ords=co_ord['pos'], ship=True)
            self.render()
            print("Use the arrow keys to move the ship")

            running_sub = True
            while running_sub:
                if keyboard.is_pressed('w'):          # Up
                    ship.move(y=1)
                    running_sub = False

                elif keyboard.is_pressed('s'):         # Down
                    ship.move(y=-1)
                    running_sub = False

                elif keyboard.is_pressed('a'):         # Left
                    ship.move(x=-1)
                    running_sub = False

                elif keyboard.is_pressed('d'):        # Right
                    ship.move(x=1)
                    running_sub = False

                elif keyboard.is_pressed('x'):       # Enter Button
                    print("wew")
                    running_sub = False


    def start(self):
        if not self.home_screen():
            sys.exit()
        else:
            self.place_ships()


game = BattleShips()
game.start()
