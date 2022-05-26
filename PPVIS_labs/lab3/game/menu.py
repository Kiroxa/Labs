from socket import gaierror
import sqlite3
import pygame
import time


class Menu:
    ''' main parent Menu class'''
    
    # sounds
    pygame.init()
    pygame.mixer.music.load('sounds/menu-music.mp3')
    pygame.mixer.music.play(-1)

    def __init__(self, game):
        ''' setup size and current game object '''
        
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        # for text
        self.game.draw_text('*', 15, 'white', self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        # refresh screen for animation
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    ''' menu at start of game '''
    
    def __init__(self, game):
        # settings
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.leaderboardx, self.leaderboardy = self.mid_w, self.mid_h + 50
        self.helpx, self.helpy = self.mid_w, self.mid_h + 70
        self.exitx, self.exity = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        # draw text and update layout
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, 'white', self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, 'white', self.startx, self.starty)
            self.game.draw_text("Leaders", 20, 'white', self.leaderboardx, self.leaderboardy)
            self.game.draw_text("Help", 20, 'white', self.helpx, self.helpy)
            self.game.draw_text("Exit", 20, 'white', self.exitx, self.exity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        ''' determine a cursor position and help it move to other position '''
        
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = 'Leaderboard'
            elif self.state == 'Leaderboard':
                self.cursor_rect.midtop = (self.helpx + self.offset, self.helpy)
                self.state = 'Help'
            elif self.state == 'Help':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Leaderboard':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Help':
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = 'Leaderboard'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.helpx + self.offset, self.helpy)
                self.state = 'Help'

    def check_input(self):
        '''when pressing ENTER '''
         
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                pygame.mixer.music.pause()
                self.game.curr_menu = None 
                self.game.playing = True
            elif self.state == 'Leaderboard':
                self.game.curr_menu = self.game.leaderboard
                print("leaderboard")
            elif self.state == 'Help':
                self.game.curr_menu = self.game.help
                print("help")
            elif self.state == 'Exit':
                exit()
            self.run_display = False


class LeaderboardMenu(Menu):
    ''' class contains database with leaders and operate with it '''
    
    _db = 'database/leaderboard.db'

    def __init__(self, game, max_leaders):    
        self.max_leaders = max_leaders
        self.leaders = self.get_leaders() 
        Menu.__init__(self, game)

    @classmethod
    def connect_database(cls):
        cls.conn = sqlite3.connect(cls._db)
        cursor = cls.conn.cursor()
        return cursor

    def get_leaders(self):
        ''' return all leaders from database '''
        
        cursor = LeaderboardMenu.connect_database()
        leaders = []
        for row in cursor.execute('SELECT * FROM leaders ORDER BY score'):
            leaders.append(row)
        return leaders[::-1]        

    def display_menu(self):
        
        self.run_display = True
        self.leaders = self.get_leaders()
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)

            text_size = 10
            padding = text_size

            self.game.draw_text('Leaderboard', text_size*3, 'darkorange', self.game.DISPLAY_W / 2, padding*2)
            padding += text_size * 5
            space = 20
            for i in range(len(self.leaders)):
                if i == 0:
                    space *= 2
                    self.draw_player(position=i, spacing=space, player=self.leaders[i], text_size=text_size*2, text_color='yellow', padding=padding)
                elif i == 1:
                    space *= 3/2
                    self.draw_player(position=i, spacing=int(space), player=self.leaders[i], text_size=text_size*3/2, text_color='gray', padding=padding)
                else:
                    self.draw_player(position=i, spacing=space, player=self.leaders[i], text_size=text_size, text_color='white', padding=padding)
                padding += text_size * 3
            self.blit_screen()

    def draw_player(self, position, spacing, player, text_size, text_color, padding):
        ''' draw every leader in the leaderboard with unique style '''
        
        self.game.draw_text(f"{position+1})" + " "*5 + player[0] + " "*5 + str(player[1]), int(text_size), text_color, self.game.DISPLAY_W / 2, padding)

    @classmethod
    def get_leader_score(cls):
        cursor = cls.connect_database()
        try:
            for x in cursor.execute("SELECT MAX(score) FROM leaders"):
                leader_score = x[0]
        except Exception as e:
            leader_score = 0
        return leader_score if leader_score else 0

    @classmethod
    def add_new_record(cls, nickname, record):
        ''' update database by adding new leader '''
        
        cursor = cls.connect_database()
        cursor.execute('''INSERT INTO leaders VALUES (?, ?)''', (nickname, record))
        cls.conn.commit()
        print("Add new record!")
        cls.conn.close()

class HelpMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)

            text_size = 10
            padding = text_size

            self.game.draw_text('Rules of the game Arkanoid', text_size, 'white', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 5/2
            self.game.draw_text('Purpose of the game', text_size, 'darkorange', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 3/2
            self.game.draw_text('To destroy all the colored panels with the ball as quickly as possible', int(text_size-2), 'orange', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 5/2
            self.game.draw_text('How to play', text_size, 'darkorange', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 3/2
            for i in ['With the help of the ( left ) ( right ) buttons of the control platform', 'Use good bonuses for yourself bad bonuses for rivals']:
                self.game.draw_text(i, int(text_size-2), 'orange', self.game.DISPLAY_W / 2, padding)
                padding += text_size * 3/2
            self.game.draw_text('to quickly break all the bricks', int(text_size-2), 'orange', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 5/2
            self.game.draw_text('Game bonuses', text_size, 'darkorange', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 3/2
            self.game.draw_text('1) Plus blocks is releases one block of blocks on your field', int(text_size-2), 'red', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 3/2
            self.game.draw_text('2) Burning ball is a ball that burns through all the blocks through', int(text_size-2), 'green', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 3/2
            self.game.draw_text('3) Platform Reducer is a surface area is reduced by 30 seconds', int(text_size-2), 'red', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 3/2
            self.game.draw_text('4) Platform Enlarger is area of the intended platform takes up 30 seconds more', int(text_size-2), 'green', self.game.DISPLAY_W / 2, padding)
            padding += text_size * 3/2
            self.game.draw_text('5) Kettlebell is slows down the action of the platform for 30 second', int(text_size-2), 'red', self.game.DISPLAY_W / 2, padding)
            self.blit_screen()


class EndMenu(Menu):
    
    def __init__(self, game):
        # settings and fonts
        Menu.__init__(self, game)
        self.font_end = pygame.font.SysFont('Arial', 40, bold=True)
        self.font_score = pygame.font.SysFont('Arial', 20, bold=True)
        # input
        self.base_font = pygame.font.SysFont('Arial', 20)
        self.record_font = pygame.font.SysFont('Arial', 32, bold=True)
        self.user_text = ''
        self.new_record = False
        

    def display_menu(self, score: int, end_label: str, end_color: str, score_label: str = "SCORE: ", score_color: str = "orange"):
        ''' drawing with displaying score '''
        
        self.run_display = True
        self.game.display.fill(self.game.BLACK)
        self.blit_screen()
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.check_events()
            # exits
            if self.game.BACK_KEY:
                pygame.mixer.music.unpause()
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.game.START_KEY:
                pygame.mixer.music.unpause()
                if self.new_record:
                    LeaderboardMenu.add_new_record(self.user_text[:-1], score)
                self.game.curr_menu = self.game.main_menu
                self.game.playing = True
                self.run_display = False
            
            render_end = self.font_end.render(end_label, 0, pygame.Color(end_color))
            render_score = self.font_score.render(score_label+str(score), 0, pygame.Color(score_color))
            self.game.window.blit(render_end, render_end.get_rect(center=(self.game.DISPLAY_W//2, self.game.DISPLAY_H//2)))
            self.game.window.blit(render_score, render_score.get_rect(center=(self.game.DISPLAY_W//2, self.game.DISPLAY_H//2+30)))
            
            if score > LeaderboardMenu.get_leader_score():
                # display new record and allow to enter your nickname
                new_record_surface = self.record_font.render("NEW RECORD!", True, (255,215,0))
                text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
                self.game.window.blit(text_surface, (self.game.DISPLAY_W//2-35, self.game.DISPLAY_H//2+60))
                self.game.window.blit(new_record_surface, new_record_surface.get_rect(center=(self.game.DISPLAY_W//2, self.game.DISPLAY_H//2-90)))
                self.new_record = True
                # print(self.user_text)
                # time.sleep(1)

            pygame.display.flip()        

    def check_input(self):
        ''' for pressing '''
        
        for event in pygame.event.get():
            pass 


if __name__ == "__main__":
    pass