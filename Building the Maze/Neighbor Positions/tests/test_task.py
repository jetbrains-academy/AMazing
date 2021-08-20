import unittest
from maze import Maze


class TestCase(unittest.TestCase):

    def test_delta_exist(self):
        maze = Maze(5, 4)
        self.assertTrue(hasattr(maze, "delta"), "Maze should have `delta` method")

    def test_delta_S(self):
        maze = Maze(5, 4)
        delta = maze.delta["S"]
        self.assertEqual((0, 1), delta)

    def test_delta_N(self):
        maze = Maze(5, 4)
        delta = maze.delta["N"]
        self.assertEqual((0, -1), delta)

    def test_delta_W(self):
        maze = Maze(5, 4)
        delta = maze.delta["W"]
        self.assertEqual((-1, 0), delta)

    def test_delta_E(self):
        maze = Maze(5, 4)
        delta = maze.delta["E"]
        self.assertEqual((1, 0), delta)
