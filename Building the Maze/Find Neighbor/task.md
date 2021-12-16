In order to visit all cells of the grid, we need to be able to find the neighbors of the 
current cell that still have all their walls (those cells have not yet been visited!).

The method `find_valid_neighbors` of the class `Maze` accepts a cell object and returns 
a list of cell objects, which are its valid neighbors. In order to determine which 
neighbors are 'valid' (in this case – the ones that still have all their walls), we need 
to check all possible offsets (defined in the `delta` variable) from this cell and assign 
the potential neighbor coordinates of the current cell plus the delta. Then we check if 
the resulting coordinates actually lie within our grid (in the interval from `0` to `nx` / `ny`), 
and if so, we get a cell at those coordinates and check whether it has all its walls 
(we previously defined methods for these two operations). If the potential neighbor 
has all its walls, we append it to the list which will be returned by the method.

### Task
Implement the `find_valid_neighbors` method of the `Maze` class as described above.


### Run
You can run the output.py to see how your code works – it should draw a PNG image 
(`neighbors.png`) of a grid with the selected cell highlighted in black and its valid 
neighbors highlighted in red. Note that one of the neighbors is not highlighted – that’s 
right, this one is not 'valid', as we have removed a wall between it and our cell.

<div class="hint">

You will need to add info about the `direction` of the valid neighbors to the list as well,
so that the in the end it consists of tuples such as, for example `('N', <cell.Cell object at 0x114a73580>)`.
</div>