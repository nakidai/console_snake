# from frame import Frame
from settings import *
from player import Player
import keyboard as kb
from out import Out
from os import system


class Game:
    def __init__(self) -> None:
        self.running = True
        self.pl = Player()
        self.out = Out()

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

        while self.running:
            try:
                self.pl.update()
                self.out.draw(self.pl)
            except IndexError as e:
                self.running = False
                print(e)


def main() -> None:
    Game().play()


if __name__ == '__main__':
    main()
