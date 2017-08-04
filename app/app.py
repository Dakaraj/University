from utils.utils import *


def main() -> None:
    clear()
    print('Welcome to university management application')
    sleep(3)
    while True:
        print('Loading data from CSV')
        read_csv()
        break
