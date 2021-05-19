from cell import Cell


class Maze:

    def __init__(self, nx, ny):
        self.nx, self.ny = nx, ny
        self.maze_grid = [[Cell(x, y) for y in range(ny)] for x in range(nx)]
