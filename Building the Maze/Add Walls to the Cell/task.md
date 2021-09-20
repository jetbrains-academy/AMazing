Cells in our maze can have a variable number of walls (up to 4) separating them from neighboring cells. 
Only cells that share a wall are considered neighbors, diagonally adjacent cells are not.


We need to be able to keep track of the present walls. An easy solution would be keeping a dictionary 
of walls for each cell object, where each key (wall) is connected with a value (`True`/`False`, depending 
on whether it’s present or absent). In our program, each cell starts with all four walls (`"N"`, `"S"`, `"E"`, `"W"`) 
in place. Later on, we will be removing some of these walls.

### Task

Let's create a dictionary `walls` where keys are directions (`"N"`, `"S"`, `"E"`, and `"W"`) and the values are 
boolean, with the `True` value when the wall exists and `False` otherwise. Initially, all cells have all
four walls.

### Run
Run `output.py` to see if you have successfully added walls to the cell. If so, it will generate a PNG 
file (`cell_walls.png`) with an image of a cell with 4 walls! Double-click the file to see the image.
