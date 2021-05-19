import unittest
from task import Maze
from cell import Cell


class TestCase(unittest.TestCase):

    def test_find_valid_neighbours_exist(self):
        maze = Maze(5, 4)
        self.assertTrue(hasattr(maze, "find_valid_neighbours"), "Maze should have `find_valid_neighbours` method")

    def test_find_valid_neighbours(self):
        maze = Maze(5, 5)
        neighbours = maze.find_valid_neighbours(Cell(2, 3))
        self.assertEqual(4, len(neighbours))
        self.assertSetEqual({"S", "N", "W", "E"}, set(map(lambda x: x[0], neighbours)))
