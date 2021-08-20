Now let’s finally put it all together and build the maze!

The algorithm should produce a path visiting each cell according to the following procedure:
1) The algorithm starts at a given cell (0, 0) and marks it as visited. To keep track of the 
  visited cells, we will use a list `cell_stack`.
2) The algorithm inspects the neighboring cells and checks if any of them are yet to be visited 
  (if they have all their walls).
3) If so, it picks one at random and moves into it, thus removing the wall between the cells.
4) The algorithm marks the new current cell as visited (adds it to the stack).
5) It increments the counter of the visited cells.
6) If the current cell doesn’t have any neighbors that haven’t been visited yet, we retract until 
  we find a cell in the stack that has an unvisited neighbor.
7) The algorithm terminates when there are no unvisited cells anymore (the `while` loop makes sure of that).


We change the `status` of the first and the last visited cell in our code for visualization purposes.


### Task

Implement steps 3 to 6 described above.

<div class='hint'>You might want to use the list method <code>pop()</code> for the retraction step. Or 
maybe you will find another way!</div>

<div class='hint'>You can use the <a href="https://docs.python.org/3/library/random.html#random.choice"><code>choice()</code></a> function from the module <code>random</code> 
(already imported!) to select a neighbor cell to move to from the list of valid neighbors.</div>

### Run

The `output.py` module produces a PNG image of your maze. To check the implementation of your maze 
generation algorithm, we suggest running your code and viewing the `maze.png` file. 


