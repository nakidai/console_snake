class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return False

        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __hash__(self) -> int:
        return int(f"{abs(self.x)}000{abs(self.y)}")

    def __str__(self) -> str:
        return f"{self.x = } | {self.y = }"
