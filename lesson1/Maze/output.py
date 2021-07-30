from cell import Cell
from task import Maze
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
        draw_cell(cel, image, color="lightgray")


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

    # Draw an image of the maze grid:
    draw_grid(maze_img, maze.maze_grid.shape[0], maze.maze_grid.shape[1])
    img.save("maze_grid.png")

