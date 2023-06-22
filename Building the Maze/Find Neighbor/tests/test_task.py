import unittest
from maze import Maze
from cell import Cell


def test_find_valid_neighbors(maze, cell):
    neighbors = []
    for direction, (dx, dy) in maze.delta.items():
        neighbor_x, neighbor_y = cell.x + dx, cell.y + dy
        if (0 <= neighbor_x < maze.nx) and (0 <= neighbor_y < maze.ny):
            neighbor = maze.cell_at(neighbor_x, neighbor_y)
            if neighbor.has_all_walls():
                neighbors.append((direction, neighbor))
    return neighbors


class TestCase(unittest.TestCase):

    def test_find_valid_neighbors_exist(self):
        maze = Maze(5, 4)
        self.assertTrue(hasattr(maze, "find_valid_neighbors"), "Maze should have `find_valid_neighbors` method")

    def test_find_valid_neighbors(self):
        maze = Maze(5, 5)
        neighbors = maze.find_valid_neighbors(Cell(2, 3))
        test_neighbors = test_find_valid_neighbors(maze, Cell(2, 3))
        self.assertEqual(4, len(neighbors), msg='The number of found neighbors is incorrect.')
        self.assertSetEqual({"S", "N", "W", "E"}, set(map(lambda x: x[0], neighbors)), msg='The neighbors found are incorrect.')
        self.assertEqual(test_neighbors, neighbors, msg = 'You should use the method cell_at to pick every next neighbor (first line in the second TODO) that has appropriate coordinates in order to check whether it has all walls.')
