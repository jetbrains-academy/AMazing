When building the maze cell-by-cell, we will need to iterate over the cells by their 
coordinates. To iterate over cell objects, we'll use the `cell_at` method of the `Maze` 
class, which will return a `Cell` at the specified position.

> In order to access the element `b` in a 3 x 3 array `my_array`, which looks something 
> like `[[a, b, c], [d, e, f], [g, h, i]]`, you need to use its row index first and 
> its column index second: `my_array[0][1]`.

### Task
Implement a function that takes coordinates `(x, y)` and returns a `Cell` object at that position.

<div class='hint'>Access the cell through the <code>maze_grid</code>.</div>


### Run
You can test how your `cell_at` method works by running `output.py` and selecting a 
cell that you wish to be highlighted. It will draw a PNG image of the grid of the 
specified size with the selected cell highlighted in black (`highlighted_cell.png`). 
