import unittest
from maze import Maze


class TestCase(unittest.TestCase):

    def test_make_maze_exist(self):
        maze = Maze(5, 4)
        self.assertTrue(hasattr(maze, "make_maze"), "Maze should have `make_maze` method")

    def test_make_maze(self):
        maze = Maze(5, 5)
        for line in maze.maze_grid:
            for cell in line:
                self.assertTrue(cell.has_all_walls())

        maze.make_maze()
        for line in maze.maze_grid:
            for cell in line:
                self.assertFalse(cell.has_all_walls())


    # TODO: need a test that all the cells are reachable