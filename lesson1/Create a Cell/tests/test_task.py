import unittest


class TestCase(unittest.TestCase):
    def test_import(self):
        try:
            from cell import Cell
        except ImportError:
            self.fail("Create a class named 'Cell'")

    def test_cell_x_y_exist(self):
        from cell import Cell
        cell = Cell(1, 5)
        self.assertTrue(hasattr(cell, "x"), "Cell should store x position in the x field")
        self.assertTrue(hasattr(cell, "y"), "Cell should store y position in the y field")

    def test_cell_x_y(self):
        from cell import Cell
        cell = Cell(1, 5)
        self.assertEqual(1, cell.x, "Assign x to the cell.x")
        self.assertEqual(5, cell.y, "Assign y to the cell.y")
