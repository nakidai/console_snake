from settings import *
from player import Player
import keyboard as kb
from out import Out
from os import system
from time import sleep


class Game:
    def __init__(self) -> None:
        self.running = True
        self.pl = Player()
        self.out = Out(self.pl)

        kb.add_hotkey(QUIT_BUTTON, self.stop_game)
        kb.add_hotkey(LEFT_BUTTON, self.pl.left)
        kb.add_hotkey(RIGHT_BUTTON, self.pl.right)
        kb.add_hotkey(UP_BUTTON, self.pl.up)
        kb.add_hotkey(DOWN_BUTTON, self.pl.down)

    def stop_game(self) -> None:
        self.running = False

    def update(self) -> None:
        pass

    def output(self) -> None:
        pass

    def play(self) -> None:
        system("clear||cls")
        time_to_sleep = 1 / FPS

        while self.running:
            try:
                sleep(time_to_sleep)
                self.pl.input()
                self.pl.update()
                self.out.draw()
            except IndexError as e:
                self.running = False
                print(e)
            except KeyboardInterrupt:
                return

        input("Press enter to leave from game")


def main() -> None:
    Game().play()


if __name__ == '__main__':
    main()
