import unittest


class TestCase(unittest.TestCase):

    def test_maze_exist(self):
        try:
            from task import Maze
        except ImportError:
            self.fail("Create a class named 'Maze'")

    def test_maze_grid_exist(self):
        from task import Maze
        maze = Maze(5, 4)
        self.assertTrue(hasattr(maze, "maze_grid"), "Maze should have `maze_grid` method")

    def test_maze_size(self):
        from task import Maze
        maze = Maze(5, 4)
        self.assertEqual(5, maze.nx)
        self.assertEqual(4, maze.ny)

    def test_maze_cells(self):
        from task import Maze
        maze = Maze(5, 4)
        self.assertEqual(5, len(maze.maze_grid))
        for line in maze.maze_grid:
            self.assertEqual(4, len(line))

