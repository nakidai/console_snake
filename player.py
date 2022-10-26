from settings import *
from point import Point
from food import Food
from time import sleep
from itertools import permutations


class Player:
    def __init__(self) -> None:
        self.direction = MAIN_DIRECTION
        self.body = [Point(MAIN_X, MAIN_Y)]

        self.food = Food(0, 0, self)
        self.food.generate_new()

        self.score = 0

    def update(self) -> None:
        sleep(1 / FPS)

        if self.direction == D_UP:
            # self.body[0].y -= 1
            self.body.append(Point(self.body[-1].x, self.body[-1].y - 1))
        elif self.direction == D_DOWN:
            # self.body[0].y += 1
            self.body.append(Point(self.body[-1].x, self.body[-1].y + 1))
        elif self.direction == D_LEFT:
            # self.body[0].x -= 1
            self.body.append(Point(self.body[-1].x - 1, self.body[-1].y))
        elif self.direction == D_RIGHT:
            # self.body[0].x += 1
            self.body.append(Point(self.body[-1].x + 1, self.body[-1].y))

        if self.body[-1] == self.food:
            self.food.generate_new()
            self.score += 1
        else:
            self.body.pop(0)

        if len(set(self.body)) != len(self.body):
            raise IndexError("Player has collision with self")

    def left(self) -> None:
        self.direction = D_LEFT

    def right(self) -> None:
        self.direction = D_RIGHT

    def up(self) -> None:
        self.direction = D_UP

    def down(self) -> None:
        self.direction = D_DOWN
