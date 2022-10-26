from settings import *
from point import Point
from food import Food


class Player:
    def __init__(self) -> None:
        self.direction = MAIN_DIRECTION
        self.body = [Point(MAIN_X, MAIN_Y)]

        self.food = Food(0, 0, self)
        self.food.generate_new()

        self.score = 1

    def input(self) -> None:
        if self.direction == D_UP:
            self.body.append(Point(self.body[-1].x, self.body[-1].y - 1))
        elif self.direction == D_DOWN:
            self.body.append(Point(self.body[-1].x, self.body[-1].y + 1))
        elif self.direction == D_LEFT:
            self.body.append(Point(self.body[-1].x - 1, self.body[-1].y))
        elif self.direction == D_RIGHT:
            self.body.append(Point(self.body[-1].x + 1, self.body[-1].y))

    def update(self) -> None:
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
