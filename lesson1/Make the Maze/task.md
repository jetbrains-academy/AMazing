The algorithm produces a path visiting each cell according to the following procedure:

- The algorithm starts at a given cell and marks it as visited.
  
- Inspect the neighbouring cells. If any of them have yet to be visited, pick one and move at random into it by removing the wall between them.

- If the current cell doesn’t have a neighbor that hasn’t been visited yet, we move back to the last cell with a not-visited neighbor.

The algorithm finished when there is no not-visited cell anymore.


### Task

Wind a way through the grid of cells at random, keeping track of the path in a `cell_stack`. 
If you end up in a dead end, simply pop visited cells off the stack until you find one with unvisited neighbours.


### Run

The `write_svg` function produces an SVG image of a maze. 
To check your maze generation algorithm implementation we suggest running your code and view the 
`maze.svg` file. 

To do so, just right-click anywhere in the **Editor** view so you can see the context menu and select **Run 'task'**.   
Alternatively, you can use the ![](execute.svg) gutter icon near the main statement. 


