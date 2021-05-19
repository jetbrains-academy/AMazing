To generate a maze, we have to randomize the traversal: meaning we pick a random but unvisited neighbor to continue our traversal. When we hit a dead end (cell with no unvisited neighbors), we 'backtrack' to the most recent cell in the stack.

The algorithm starts at a given cell and marks it as visited. It selects a random neighboring cell that hasn’t been visited yet and makes that one the current cell, marks it as visited, and so on.

If the current cell doesn’t have a neighbor that hasn’t been visited yet, we move back to the last cell with a not-visited neighbor.

The algorithm finished when there is no not-visited cell anymore.

И рассказываем, что посмотреть результат можно с помощью специальной функции.
