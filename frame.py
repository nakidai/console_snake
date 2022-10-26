from settings import *
from sys import platform

if platform == "win32":
    from ctypes import *
    STD_OUTPUT_HANDLE = -11
    STDHANDLE = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    class COORDSET(Structure):
        _fields_ = [("X", c_long), ("Y", c_long)]

    def _set_cursor_position(x: int, y: int) -> None:
        windll.kernel32.SetConsoleCursorPosition(STDHANDLE, COORDSET(x, y))
else:
    def _set_cursor_position(x: int, y: int) -> None:
        print(f"\033[{x};{y}H")


class Frame:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.matrix = [[SPACE] * width for line in range(height)]

    def __str__(self) -> str:
        out_string = f"Width:\n  {self.width}\n"
        out_string += f"Height:\n  {self.height}\n"
        return out_string

    def draw(
        self, x: int, y: int,
        value: int = WALL,
        width: int = 1, height: int = 1
    ) -> None:
        if not isinstance(value, int):
            raise TypeError("Value must be int")

        for line in range(height):
            for column in range(width):
                self.matrix[y + line][x + column] = value

    def show(self) -> None:
        _set_cursor_position(0, 0)

        out_string = f"┍{'━' * (self.width * 2)}┑\n"

        for line in self.matrix:
            to_str = ''

            to_str += '│'
            for elem in line:
                if elem == SPACE:
                    to_str += "  "
                elif elem == WALL:
                    to_str += "██"
                elif elem == FOOD:
                    to_str += "@@"
                elif elem == WALL_FOOD:
                    to_str += "@█"
            to_str += '│\n'

            out_string += to_str
        out_string += f"┕{'━' * (self.width * 2)}┙"

        print(out_string)

    def see(self, x, y) -> str:
        return self.matrix[y][x]
