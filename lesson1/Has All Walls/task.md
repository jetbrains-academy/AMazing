During the maze creation process, all cells in the maze need to be visited, so in the end, 
there should be no remaining cells with all four walls in place. Therefore, at some point, 
we'll need to check whether a cell still has all its walls in order to figure out which 
cells we can visit next.

### Task

Let’s define a method that will check if all values in the `self.walls` dictionary are `True`.

<div class="hint">You could try using the <a href="https://docs.python.org/3/library/functions.html#all"><code>all</code></a> built-in function.</div>

### Run
Run `output.py` to see if you have successfully implemented the method. It should print `True` 
if the cell has all the walls and `False` if not. It will also draw an image of a cell 
(`cell_walls.png`). Try setting one of the walls to `False` and running `output.py` to make 
sure that it is not there. Note that in order to pass the test on this task, you will need to 
set all 4 walls back to `True` after you’re done with the visualization. 
