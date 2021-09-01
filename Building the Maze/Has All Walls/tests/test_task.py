import unittest
from cell import Cell


class TestCase(unittest.TestCase):

    def test_cell_has_all_walls_exist(self):
        cell = Cell(1, 5)
        self.assertTrue(hasattr(cell, "has_all_walls"), "Cell should have `has_all_walls` method")

    def test_cell_has_all_walls(self):
        cell = Cell(1, 5)
        self.assertTrue(cell.has_all_walls(), "Newly created cell should have all walls")

    def test_cell_wall_destroyed(self):
        cell = Cell(1, 5)
        cell.walls['N'] = False
        self.assertFalse(cell.has_all_walls(), "`has_all_walls` method should return false when wall is destroyed")
