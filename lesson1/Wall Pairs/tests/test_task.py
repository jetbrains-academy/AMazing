import unittest
from cell import Cell


class TestCase(unittest.TestCase):

    def test_wall_pairs_exist(self):
        cell = Cell(1, 5)
        self.assertTrue(hasattr(cell, "wall_pairs"), "Cell should have `wall_pairs` field")

    def test_wall_pairs(self):
        cell = Cell(1, 5)
        self.assertEqual('W', cell.wall_pairs['E'], "Pair for the west wall should be east")
        self.assertEqual('E', cell.wall_pairs['W'], "Pair for the east wall should be west")
        self.assertEqual('S', cell.wall_pairs['N'], "Pair for the south wall should be north")
        self.assertEqual('N', cell.wall_pairs['S'], "Pair for the north wall should be south")
