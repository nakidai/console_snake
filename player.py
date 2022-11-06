from settings import *
from point import Point
from food import Food


class Player:
    def __init__(self, game) -> None:
        self.direction = MAIN_DIRECTION
        self.body = [Point(MAIN_X, MAIN_Y)]

        self.food = Food(0, 0)
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

    def _check_collision(body: list[Point]) -> None:
        for point in body:
            if point.x < 0 or point.y < 0:
                raise IndexError("Snake has collision with walls")
            elif point.x >= WIDTH or point.y >= HEIGHT:
                raise IndexError("Snake has collision with walls")

        if len(set(body)) != len(body):
            raise IndexError("Player has collision with self")

    def update(self) -> None:
        if self.body[-1] == self.food:
            self.food.generate_new()
            self.score += 1
        else:
            self.body.pop(0)

        Player._check_collision(self.body)

    def left(self, game) -> None:
        if not game.is_pause and self.direction != D_RIGHT:
            self.direction = D_LEFT

    def right(self, game) -> None:
        if not game.is_pause and self.direction != D_LEFT:
            self.direction = D_RIGHT

    def up(self, game) -> None:
        if not game.is_pause and self.direction != D_DOWN:
            self.direction = D_UP

    def down(self, game) -> None:
        if not game.is_pause and self.direction != D_UP:
            self.direction = D_DOWN
