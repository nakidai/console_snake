from settings import *
from player import Player
import keyboard as kb
from out import Out
from os import system
from time import sleep, time


class Game:
    def __init__(self) -> None:
        self.running = True
        self.is_pause = False
        self.pl = Player()
        self.out = Out(self.pl)

        kb.add_hotkey(QUIT_BUTTON, self.stop_game)
        kb.add_hotkey(PAUSE_BUTTON, self.switch_pause)
        kb.add_hotkey(
            LEFT_BUTTON,
            self.pl.left,
            args=[self]
        )
        kb.add_hotkey(
            RIGHT_BUTTON,
            self.pl.right,
            args=[self]
        )
        kb.add_hotkey(
            UP_BUTTON,
            self.pl.up,
            args=[self]
        )
        kb.add_hotkey(
            DOWN_BUTTON,
            self.pl.down,
            args=[self]
        )

    def switch_pause(self) -> None:
        self.is_pause = not self.is_pause

    def stop_game(self) -> None:
        if not self.is_pause:
            self.running = False

    def play(self) -> None:
        system("clear||cls")
        print()

        start_time = time()
        different_between_time = 1 / FPS

        while self.running:
            try:
                sleep(1 / FPS - different_between_time)
                start_time = time()

                if not self.is_pause:
                    self.pl.input()
                    self.pl.update()
                    self.out.draw()

                end_time = time()
                different_between_time = start_time - end_time

            except IndexError as e:
                self.running = False
                print(e)
            except KeyboardInterrupt:
                return

        input("Press enter to leave from game.\n")


def main() -> None:
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
