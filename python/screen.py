from typing import List, Tuple

class Screen:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def draw(self, cells: List[bool]):
        assert len(cells) == self.size_1d, "cells list size does not match screen size"
        for i in range(self.height):
            for j in range(self.width):
                if cells[(i*self.width)+j]:
                    print("██", end="")
                else:
                    print("  ", end="")
            print("")

    @property
    def size_1d(self) -> int:
        return self.height * self.width

    @property
    def size_2d(self) -> Tuple[int, int]:
        return self.height, self.width
