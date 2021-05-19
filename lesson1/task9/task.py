from cell import Cell


class Maze:
    delta = {'N': (0, -1),
             'S': (0, 1),
             'W': (-1, 0),
             'E': (1, 0)}

    def __init__(self, nx, ny, ix=0, iy=0):
        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.maze_grid = [[Cell(x, y) for y in range(ny)] for x in range(nx)]

    def cell_at(self, x, y):
        return self.maze_grid[x][y]

    def find_valid_neighbours(self, cell):
        neighbours = []
        for direction, (dx, dy) in self.delta.items():
            neighbour_x, neighbour_y = cell.x + dx, cell.y + dy
            if (0 <= neighbour_x < self.nx) and (0 <= neighbour_y < self.ny):
                neighbour = self.cell_at(neighbour_x, neighbour_y)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours
