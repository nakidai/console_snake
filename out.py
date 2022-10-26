from settings import *
from player import Player
from frame import Frame


class Out:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = FPS

    def draw(self, pl: Player) -> None:
        frame = Frame(self.width, self.height)

        for point in pl.body:
            if point.x < 0 or point.y < 0:
                raise IndexError("Snake has collision with walls")
            elif point.x >= WIDTH or point.y >= HEIGHT:
                raise IndexError("Snake has collision with walls")

            frame.draw(
                x=point.x, y=point.y,
                value=WALL,
                width=1, height=1
            )

        if frame.see(pl.food.x, pl.food.y) == WALL:
            frame.draw(
                x=pl.food.x, y=pl.food.y,
                value=WALL_FOOD
            )
        else:
            frame.draw(
                x=pl.food.x, y=pl.food.y,
                value=FOOD
            )

        frame.show()
