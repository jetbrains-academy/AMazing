import unittest
import random
import numpy as np
from maze import Maze
from cell import Cell


def find_valid_neighbors(maze_, cell_):
    neighbors = []
    for direction, (dx, dy) in maze_.delta.items():
        neighbor_x, neighbor_y = cell_.x + dx, cell_.y + dy
        if (0 <= neighbor_x < maze_.nx) and (0 <= neighbor_y < maze_.ny):
            neighbor = maze_.cell_at(neighbor_x, neighbor_y)
            # Check if the neighbor does not have the wall between it and the curr. cell
            if not neighbor.walls[Cell.wall_pairs[direction]]:
                neighbors.append((direction, neighbor))
    return neighbors


def test_reachable(maze):
    idx1 = np.random.randint(maze.nx, size=2)
    idx2 = np.random.randint(maze.nx, size=2)
    # Prevent start and destination from being the same cell:
    while True:
        if idx2[0] != idx1[0] or idx2[1] != idx1[1]:
            break
        else:
            idx2 = np.random.randint(maze.nx, size=2)
    current_cell = maze.maze_grid[idx1[0]][idx1[1]]
    destination = maze.maze_grid[idx2[0]][idx2[1]]

    n = maze.nx * maze.ny
    cell_stack = []
    counter = 0

    while counter < n * 1000:
        neighbors = find_valid_neighbors(maze, current_cell)
        counter += 1
        # If no neighbors not separated by wall are found - retract
        if not neighbors:
            try:
                current_cell = cell_stack.pop()
                continue
            except IndexError:
                return False

        direction, next_cell = random.choice(neighbors)
        cell_stack.append(current_cell)
        current_cell = next_cell

        if current_cell == destination:
            return True
    else:
        return False


class TestCase(unittest.TestCase):

    def test_make_maze(self):
        maze = Maze(10, 10, (0, 0))
        for line in maze.maze_grid:
            for cell in line:
                self.assertFalse(cell.has_all_walls(), msg="There should be no cells with all walls still present "
                                                           "when you complete building the maze.")

    def test_make_maze_2(self):
        maze = Maze(10, 10, (0, 0))
        no_walls = []
        for line in maze.maze_grid:
            for cell in line:
                walls = [wall for wall in cell.walls.values()]
                if walls == [False, False, False, False]:
                    no_walls.append(walls)
        print(no_walls)
        if len(no_walls) == 64:
            self.fail(msg="It seems all or most of the internal walls have been knocked down. That is not "
                          "right.")

    def test_reachable(self):
        maze_ = Maze(10, 10, (0, 0))
        test_ = [True if test_reachable(maze_) else False for i in range(100)]
        self.assertTrue(all(test_), msg='Some cells appear unreachable in your maze :('
                                        'This could happen if not all of the grid cells were visited '
                                        'by your algorithm, or if walls were not knocked down.'
                                        'Make sure both of these things happen. Visualization could'
                                        'also be helpful.')
