from cell import Cell
from maze import Maze
from PIL import Image, ImageDraw


def draw_cell(cell, image, color="black", wide=5):
    # Cell coordinates on the image calculated from its (x, y) coordinates,
    # cell side length (100 pt), image margin (90 pt) and line thickness (10 pt).
    x = margin + line_thickness + cell.x * cell_side
    y = margin + line_thickness + cell.y * cell_side

    north, south, east, west = [(x - cell_side / 2, y - cell_side / 2), (x + cell_side / 2, y - cell_side / 2)], \
                               [(x - cell_side / 2, y + cell_side / 2), (x + cell_side / 2, y + cell_side / 2)], \
                               [(x + cell_side / 2, y - cell_side / 2), (x + cell_side / 2, y + cell_side / 2)], \
                               [(x - cell_side / 2, y - cell_side / 2), (x - cell_side / 2, y + cell_side / 2)]
    lines = north, south, east, west
    shown_walls = [i for (i, v) in zip(lines, cell.walls.values()) if v]
    for wall in shown_walls:
        image.line(wall, fill=color, width=wide)


def draw_grid(image, x_cells, y_cells):
    cells_ = {}
    count = 0
    for i in range(x_cells):
        for j in range(y_cells):
            cell_name = "Cell%d" % count
            count += 1
            cells_[cell_name] = Cell(i, j)
    for cel in cells_.values():
        draw_cell(cel, image, "lightgray")


if __name__ == '__main__':
    dim1 = int(input('Enter x dimension: '))
    dim2 = int(input('Enter y dimension: '))
    margin = 80
    cell_side = 100
    line_thickness = 10
    maze = Maze(dim1, dim2)
    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)
    img = Image.new("RGB", (width, height), (255, 255, 255))
    maze_img = ImageDraw.Draw(img)
    draw_grid(maze_img, maze.maze_grid.shape[0], maze.maze_grid.shape[1])
    highlighted_cell = maze.cell_at(int(input('Enter x coordinate of cell to highlight: ')),
                                    int(input('Enter y coordinate of cell to highlight: ')))
    # Find all neighbors
    neighbors = maze.find_valid_neighbors(highlighted_cell)

    # Knock down a wall with one of the neighbors
    highlighted_cell.knock_down_wall(neighbors[0][1], neighbors[0][0])

    # Re-address the list of valid neighbors (the one without a wall shouldn't be there!)
    neighbors = maze.find_valid_neighbors(highlighted_cell)

    # Illustrate this
    draw_cell(highlighted_cell, maze_img)
    for neighbor in neighbors:
        draw_cell(neighbor[1], maze_img, color="red", wide=2)

    img.save('neighbors.png')
