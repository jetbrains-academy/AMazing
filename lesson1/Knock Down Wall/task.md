To create a maze from a grid of unconnected cells, we need to eliminate many walls.
We will start from the cell at `(0, 0)` and traverse the grid. Whenever a new cell is 
visited, the wall between the new cell and the previous one is removed. You can imagine 
something actually moving from one cell to another and physically knocking the walls down.

Again, all the cells need to be visited at least once so that none of them have 
all four walls standing when the algorithm terminates.

### Task

In this task, we will implement the method `knock_down_wall` of the class `Cell`. It 
accepts two cells – a current cell (`self`) and its neighbor (`other`) to which we will be 
moving next, as well as the `wall` between them. First, the method removes the `wall` of 
the current cell by setting it to `False`. Then we need to remove (set to `False`) a 
corresponding wall of the `other` cell. The function should pick the proper wall using 
the previously created dictionary `wall_pairs`.

<div class='hint'>Access the required wall of the <code>other</code> cell by looking up 
<code>wall</code> in <code>wall_pairs</code> of the class <code>Cell</code>.</hint>

### Run
Run `output.py` to see if you have successfully implemented the method. It will draw 
two images of two cells (`adjacent_cells.png` and `removed_NS_wall.png`). The first 
one shows the cells before a wall is knocked down, and the second one – after. The code 
also prints the `walls` dictionary for each cell.
