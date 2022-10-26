from point import Point
from random import randint
from settings import *


class Food(Point):
    def __init__(self, x, y, pl):
        Point.__init__(self, x, y)
        self.pl = pl

    def generate_new(self) -> None:
        self.x = randint(0, WIDTH - 1)
        self.y = randint(0, HEIGHT - 1)
