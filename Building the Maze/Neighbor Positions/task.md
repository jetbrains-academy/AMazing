Another crucial step is finding all adjacent cells. In our paradigm, the cell to the north of 
the current one (if present) has an offset of `-1` along the y-axis and a `0` offset along the 
x-axis. That is, a neighbor to the north would have an offset `(0, -1)`.

### Task
Your task is to complete the `delta` class variable of the `Maze` so that it contains all possible offsets.

<div class="hint">You need to add <code>"W"</code> and <code>"E"</code>.</div>
