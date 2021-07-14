from cell import Cell
from task import Maze
from PIL import Image, ImageDraw, ImageFont


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
    if cell.status == 'Start' or cell.status == 'End':
        # font = ImageFont.load_default()  # Uncomment this if font loading fails
        font = ImageFont.truetype("Arial Unicode.ttf", 18)  # Comment this if font loading fails
        image.text((x - 25, y - 10), cell.status.upper(), (255, 0, 0), font=font)


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


def draw_image(image, filename, cells):
    img1 = ImageDraw.Draw(image)
    draw_grid(img1, cells.shape[0], cells.shape[1])
    for cell in cells.flatten():
        draw_cell(cell, img1)
    image.show()
    image.save(filename)


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
    maze.make_maze()
    w, h = (80 + 100 * dim for dim in maze.maze_grid.shape)
    img = Image.new("RGB", (w, h), (255, 255, 255))

    draw_image(img, "maze.png", maze.maze_grid)
