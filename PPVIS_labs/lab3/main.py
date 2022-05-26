from game.game import Game


def main():
    ''' apply game settings from file and start game loop '''
    
    g = Game(settings_file='./game/settings.json')
    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()


if __name__ == "__main__":
    main()