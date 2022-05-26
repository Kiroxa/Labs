
from random import randrange as rnd
from .bonus_rect import BonusRect


class Blocks:
    ''' class Block create a matrix ob rainbow blocks '''
    
    def __init__(self, level_settings: list, sizes: list) -> None:
        self.lines = len(level_settings)
        self.blocks_in_line = len(level_settings[0])
        self.sizes = sizes
        self.block_list = self.fill_block_list(level_settings, sizes)
        self.color_list = []
        for _ in range(self.lines):
            line_color = (rnd(30, 256), rnd(30, 256), rnd(30, 256))
            self.color_list += [line_color for i in range(self.blocks_in_line)]

    def fill_block_list(self, level_settings, sizes):
        ''' fill created block in matrix to represent in the game '''
        
        blocks_list = []
        for i in range(self.lines):
            for j in range(self.blocks_in_line):
                if level_settings[i][j] == '0':
                    blocks_list.append(0)
                else:        
                    blocks_list.append(BonusRect(15 + 52 * j, 50 + 22 * i, int(sizes[0]), int(sizes[1]), level_settings[i][j]))
                # print(blocks_list)
        return blocks_list
