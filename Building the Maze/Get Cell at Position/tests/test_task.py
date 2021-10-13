import unittest
from maze import Maze


class TestCase(unittest.TestCase):

    def test_cell_at_exist(self):
        maze = Maze(5, 4)
        self.assertTrue(hasattr(maze, "cell_at"), "Maze should have `cell_at` method")

    def test_random_cell_at(self):
        maze = Maze(5, 4)
        cell = maze.cell_at(2, 3)
        self.assertEqual(2, cell.x)
        self.assertEqual(3, cell.y)
