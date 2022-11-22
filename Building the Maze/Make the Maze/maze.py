import random
import numpy as np
from cell import Cell


class Maze:
    delta = {'N': (0, -1),
             'S': (0, 1),
             'W': (-1, 0),
             'E': (1, 0)}

    def __init__(self, nx, ny, start_):
        self.nx, self.ny = nx, ny
        self.maze_grid = np.array([[Cell(x, y) for y in range(ny)] for x in range(nx)])
        self.__make_maze(start_)

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

    def __make_maze(self, start_coords):
        n = self.nx * self.ny
        cell_stack = []
        # current_cell = self.cell_at(0, 0)
        current_cell = self.cell_at(start_coords[0], start_coords[1])
        current_cell.status = 'Start'
        n_visited = 1

        while n_visited < n:
            neighbors = self.find_valid_neighbors(current_cell)

            if not neighbors:
                current_cell = cell_stack.pop()
                continue

            direction, next_cell = random.choice(neighbors)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            n_visited += 1
            if n_visited == n:
                current_cell.status = 'End'
