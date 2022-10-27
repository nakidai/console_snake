from settings import *
from player import Player
from frame import Frame


class Out:
    def __init__(self, pl: Player) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.pl = pl

    def draw(self) -> None:
        frame = Frame(self.width, self.height)
        pl = self.pl

        for point in pl.body:
            frame.draw(
                x=point.x, y=point.y,
                value=WALL,
                width=1, height=1
            )

        frame.draw(
            x=pl.body[-1].x, y=pl.body[-1].y,
            value=HEAD,
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
        print(f"Score: {pl.score}")
