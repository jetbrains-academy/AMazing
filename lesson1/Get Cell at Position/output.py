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
        draw_cell(cel, image, "lightgray")


def get_dimensions(*cells):
    return max([cell.x for cell in cells]) + 1, max([cell.y for cell in cells]) + 1


def generate_cells(x, y):
    cells_ = {}
    count = 0
    for i in range(x):
        for j in range(y):
            cell_name = "Cell%d" % count
            count += 1
            cells_[cell_name] = Cell(i, j)
    return cells_


if __name__ == '__main__':
    dim1 = int(input('Enter x dimension: '))
    dim2 = int(input('Enter y dimension: '))
    maze = Maze(dim1, dim2)

    # Print the cell selected using the method defined in the task
    print(maze.cell_at(dim1 - 1, dim2 - 1))

    w, h = (80 + 100 * dim for dim in maze.maze_grid.shape)
    img = Image.new("RGB", (w, h), (255, 255, 255))
    img1 = ImageDraw.Draw(img)
    draw_grid(img1, maze.maze_grid.shape[0], maze.maze_grid.shape[1])

    # Highlight the cell selected using the method defined in the task
    highlighted_cell = maze.cell_at(int(input('Enter x coordinate of cell to highlight: ')),
                                    int(input('Enter y coordinate of cell to highlight: ')))
    draw_cell(highlighted_cell, img1)

    img.save('highlighted_cell.png')
