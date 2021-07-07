from cell import Cell
import numpy as np


class Maze:

    def __init__(self, nx, ny):
        self.nx, self.ny = nx, ny
        self.maze_grid = np.array([[Cell(x, y) for y in range(ny)] for x in range(nx)])
