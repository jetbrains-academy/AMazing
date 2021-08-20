A wall separates a pair of cells in the N-S or W-E directions.
When a cell has a wall `"S"` and an adjacent cell to the south, then the adjacent cell 
must have a wall `"N"`, which is, essentially, the same wall. In our code, however, we 
need to create this connection to make sure that when we remove an `"S"` wall from a cell 
that has an `"S"` neighbor, the neighbor would lose its `"N"` wall automatically 
(and not some other wall!).

We will store information about corresponding walls in the dictionary `wall_pairs`, 
which is a class attribute because this relationship should be true for all instances 
of the class `Cell`.

### Task

Add missing wall pairs (`key:value` pairs) to the `wall_pairs` dictionary. The first 
two pairs have already been defined.