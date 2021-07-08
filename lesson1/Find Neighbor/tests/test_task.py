import unittest
from task import Maze
from cell import Cell


class TestCase(unittest.TestCase):

    def test_find_valid_neighbors_exist(self):
        maze = Maze(5, 4)
        self.assertTrue(hasattr(maze, "find_valid_neighbors"), "Maze should have `find_valid_neighbors` method")

    def test_find_valid_neighbors(self):
        maze = Maze(5, 5)
        neighbors = maze.find_valid_neighbors(Cell(2, 3))
        self.assertEqual(4, len(neighbors))
        self.assertSetEqual({"S", "N", "W", "E"}, set(map(lambda x: x[0], neighbors)))
