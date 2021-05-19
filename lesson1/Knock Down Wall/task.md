To go from a grid of unconnected cells to a maze we need to knock down some walls. We'll choose a cell to start from and traverse the grid. 
Whenever a new cell is visited, the wall between the new cell and the previous cell is knocked down.

### Task

Write a function to knock down the wall between cells `self` and `other`. This function should pick the proper wall using previously created `wall_pairs`.
