import unittest
from cell import Cell


class TestCase(unittest.TestCase):

    def test_knock_down_wall_exist(self):
        cell = Cell(1, 5)
        self.assertTrue(hasattr(cell, "knock_down_wall"), "Cell should have `knock_down_wall` field")

    def test_knock_down_wall_S(self):
        cell1 = Cell(1, 5)
        cell2 = Cell(2, 5)
        cell1.knock_down_wall(cell2, 'S')
        self.assertFalse(cell2.walls['N'], "Knock down should destroy according wall for the other cell")

    def test_knock_down_wall_N(self):
        cell1 = Cell(1, 5)
        cell2 = Cell(2, 5)
        cell1.knock_down_wall(cell2, 'N')
        self.assertFalse(cell2.walls['S'], "Knock down should destroy according wall for the other cell")

    def test_knock_down_wall_W(self):
        cell1 = Cell(1, 5)
        cell2 = Cell(2, 5)
        cell1.knock_down_wall(cell2, 'W')
        self.assertFalse(cell2.walls['E'], "Knock down should destroy according wall for the other cell")

    def test_knock_down_wall_E(self):
        cell1 = Cell(1, 5)
        cell2 = Cell(2, 5)
        cell1.knock_down_wall(cell2, 'E')
        self.assertFalse(cell2.walls['W'], "Knock down should destroy according wall for the other cell")
