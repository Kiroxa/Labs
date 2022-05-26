from pygame import Rect


class BonusRect(Rect):
    ''' special block that contains bonuses '''
    
    def __init__(self, x_pos, y_pos, x, y, bonus_index: str):
        super().__init__(x_pos, y_pos, x, y)
        self.bonus_index = bonus_index 

