import unittest
from task import Cell


class TestCase(unittest.TestCase):

    def test_cell_walls_exist(self):
        cell = Cell(1, 5)
        self.assertTrue(hasattr(cell, "walls"), "Cell should store walls in the walls field")

    def test_cell_walls_size(self):
        cell = Cell(1, 5)
        self.assertEqual(4, len(cell.walls), "There should be exactly 4 walls in cell")

    def test_cell_walls_values(self):
        cell = Cell(1, 5)
        self.assertEqual(True, cell.walls['N'], "The north wall exist by default")
        self.assertEqual(True, cell.walls['S'], "The south wall exist by default")
        self.assertEqual(True, cell.walls['E'], "The east wall exist by default")
        self.assertEqual(True, cell.walls['W'], "The west wall exist by default")
