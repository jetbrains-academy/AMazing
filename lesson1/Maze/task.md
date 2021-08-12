It's now time to start creating our maze! As it was mentioned before, we can represent 
a maze as a grid of `nx` x `ny` interconnected cells and it will be constructed starting 
at the cell indexed at `(0, 0)`. First, we will create the grid itself and visualize it.


We will now need a new class, `Maze`, defined in a separate module `maze.py`. The `__init__()` 
method of the class `Maze` will initialize the maze object, its `x` and `y` dimensions (measured 
in the number of cells along the corresponding axis), and the maze grid in the form of a 
[NumPy](https://numpy.org/doc/stable/user/whatisnumpy.html) array.

> A [NumPy array](https://numpy.org/doc/stable/reference/generated/numpy.array.html) is a grid of values (all of the same type). It is indexed by nonnegative 
> integers. The number of dimensions is the rank of the array (we will be working with a rank 2 
> array); the `shape` of an array is a tuple of integers giving the size of the array along each 
> dimension. We can initialize NumPy arrays from nested lists and access elements 
> using square brackets.

### Task
Complete the line of the `__init__()`  method to initialize the `maze_grid`.

<div class='hint'>It would be convenient to use <a href="https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions">list comprehension</a>.</div> 

### Run
Run `output.py` to see if you have successfully implemented the method. It will 
draw a PNG image of the grid (`maze_grid.png`). 

