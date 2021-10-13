from cell import Cell
import numpy as np


class Maze:
    delta = {'N': (0, -1),
             'S': (0, 1),
             'W': (-1, 0),
             'E': (1, 0)}

    def __init__(self, nx, ny):
        self.nx, self.ny = nx, ny
        self.maze_grid = np.array([[Cell(x, y) for y in range(ny)] for x in range(nx)])

    def cell_at(self, x, y):
        return self.maze_grid[x][y]
