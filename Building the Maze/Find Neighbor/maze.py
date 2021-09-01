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

    def find_valid_neighbors(self, cell):
        neighbors = []
        for direction, (dx, dy) in self.delta.items():
            neighbor_x, neighbor_y = cell.x + dx, cell.y + dy
            if (0 <= neighbor_x < self.nx) and (0 <= neighbor_y < self.ny):
                neighbor = self.cell_at(neighbor_x, neighbor_y)
                if neighbor.has_all_walls():
                    neighbors.append((direction, neighbor))
        return neighbors
