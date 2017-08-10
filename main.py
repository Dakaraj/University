from app.app import App
from utils.utils import *

if __name__ == '__main__':
    app: App = App()
    try:
        app.main_loop()
    except (KeyboardInterrupt, EOFError):
        while True:
            clear()
            print('############ EXIT PROGRAM ############\n\n'
                  'Do you wish to save all your data?\n'
                  '1. Save and exit\n'
                  '2. Discard all changes and exit\n')
            user_input: str = input('>')
            if user_input == '1':
                p_list: list = app.persons_list
                save_data_and_exit(p_list)
            elif user_input == '2':
                break
            else:
                continue

        clear()
        print('Thank you for using this program')
        quit()
