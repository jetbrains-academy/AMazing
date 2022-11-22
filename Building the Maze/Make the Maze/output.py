from cell import Cell
from maze import Maze
from PIL import Image, ImageDraw, ImageFont


def draw_cell(cell, image, color="black", wide=5):
    # Cell coordinates on the image calculated from its (x, y) coordinates,
    # cell side length (100 pt), image margin (90 pt) and line thickness (10 pt).
    x = margin + line_thickness + cell.x * cell_side
    y = margin + line_thickness + cell.y * cell_side

    lines = [(x - cell_side / 2, y - cell_side / 2), (x + cell_side / 2, y - cell_side / 2)], \
            [(x - cell_side / 2, y + cell_side / 2), (x + cell_side / 2, y + cell_side / 2)], \
            [(x + cell_side / 2, y - cell_side / 2), (x + cell_side / 2, y + cell_side / 2)], \
            [(x - cell_side / 2, y - cell_side / 2), (x - cell_side / 2, y + cell_side / 2)]

    shown_walls = [i for (i, v) in zip(lines, cell.walls.values()) if v]
    for wall in shown_walls:
        image.line(wall, fill=color, width=wide)
    if cell.status == 'Start' or cell.status == 'End':
        try:
            font = ImageFont.truetype("Arial Unicode.ttf", 18)
            image.text((x - 25, y - 10), cell.status.upper(), (255, 0, 0), font=font)
        except OSError:
            font = ImageFont.load_default()
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


def draw_image(image, filename, cells):
    maze_img = ImageDraw.Draw(image)
    draw_grid(maze_img, cells.shape[0], cells.shape[1])
    for cell in cells.flatten():
        draw_cell(cell, maze_img)
    image.save(filename)


if __name__ == '__main__':
    dimension1 = int(input('Enter x dimension: '))
    dimension2 = int(input('Enter y dimension: '))
    start_x = int(input('Enter x coordinate of the start: '))
    start_y = int(input('Enter y coordinate of the start: '))

    margin = 80
    cell_side = 100
    line_thickness = 10
    maze = Maze(dimension1, dimension2, [start_x, start_y])
    # maze.make_maze()
    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)
    img = Image.new("RGB", (width, height), (255, 255, 255))

    draw_image(img, "maze.png", maze.maze_grid)
