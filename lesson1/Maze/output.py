from cell import Cell
from task import Maze
from PIL import Image, ImageDraw


def draw_cell(cell, image, color="black", wide=5):
    filt = [x for x in cell.walls.values()]
    x = 90 + cell.x * 100
    y = 90 + cell.y * 100

    north, south, east, west = [(x - 50, y - 50), (x + 50, y - 50)], \
                               [(x - 50, y + 50), (x + 50, y + 50)], \
                               [(x + 50, y - 50), (x + 50, y + 50)], \
                               [(x - 50, y - 50), (x - 50, y + 50)]
    lines = north, south, east, west
    filtered_lines = [i for (i, v) in zip(lines, filt) if v]
    for line in filtered_lines:
        image.line(line, fill=color, width=wide)


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
    maze = Maze(dim1, dim2)
    w, h = (80 + 100 * dim for dim in maze.maze_grid.shape)
    img = Image.new("RGB", (w, h), (255, 255, 255))
    img1 = ImageDraw.Draw(img)

    # Draw an image of the maze grid:
    draw_grid(img1, maze.maze_grid.shape[0], maze.maze_grid.shape[1])
    img.save("maze_grid.png")

