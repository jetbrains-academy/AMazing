import random
import numpy as np
from cell import Cell


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

    def find_valid_neighbours(self, cell):
        neighbours = []
        for direction, (dx, dy) in self.delta.items():
            neighbour_x, neighbour_y = cell.x + dx, cell.y + dy
            if (0 <= neighbour_x < self.nx) and (0 <= neighbour_y < self.ny):
                neighbour = self.cell_at(neighbour_x, neighbour_y)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def write_svg(self, filename):
        """Write an SVG image of the maze to filename."""
        scy, scx = 500 / self.ny, 500 / self.nx

        def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
            ww_f.write(f'<line x1="{ww_x1}" y1="{ww_y1}" x2="{ww_x2}" y2="{ww_y2}"/>')

        with open(filename, 'w') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>')
            f.write('<svg xmlns="http://www.w3.org/2000/svg"')
            f.write('    xmlns:xlink="http://www.w3.org/1999/xlink"')
            f.write('    width="520" height="520" viewBox="-10 -10 520 520">')
            f.write('<defs>\n<style type="text/css"><![CDATA[')
            f.write('line {')
            f.write('    stroke: #000000;\n    stroke-linecap: square;')
            f.write('    stroke-width: 5;\n}')
            f.write(']]></style>\n</defs>')

            for x in range(self.nx):
                for y in range(self.ny):
                    if self.cell_at(x, y).walls['S']:
                        x1, y1, x2, y2 = x * scx, (y + 1) * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
                    if self.cell_at(x, y).walls['E']:
                        x1, y1, x2, y2 = (x + 1) * scx, y * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)

            f.write('<line x1="0" y1="0" x2="500" y2="0"/>')
            f.write('<line x1="0" y1="0" x2="0" y2="500"/>')
            f.write('</svg>')

    def make_maze(self):
        n = self.nx * self.ny
        cell_stack = []
        current_cell = self.cell_at(0, 0)
        current_cell.status = 'Start'
        n_visited = 1

        while n_visited < n:
            neighbours = self.find_valid_neighbours(current_cell)

            if not neighbours:
                current_cell = cell_stack.pop()
                continue

            direction, next_cell = random.choice(neighbours)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            n_visited += 1
            if n_visited == n:
                current_cell.status = 'End'


if __name__ == '__main__':
    dim1 = int(input('Enter x dimension: '))
    dim2 = int(input('Enter y dimension: '))
    maze = Maze(dim1, dim2)
    # maze = Maze(5, 5)
    maze.make_maze()
    maze.write_svg("maze.svg")
