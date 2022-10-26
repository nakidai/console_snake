class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            raise TypeError("You can compare only Point with Point")

    def __hash__(self) -> int:
        return int(f"{abs(self.x)}000{abs(self.y)}")

    def __str__(self) -> str:
        return f"{self.x = } | {self.y = }"
