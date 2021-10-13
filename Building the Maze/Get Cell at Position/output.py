from cell import Cell
from maze import Maze
from PIL import Image, ImageDraw


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
    dimension1 = int(input('Enter x dimension: '))
    dimension2 = int(input('Enter y dimension: '))
    margin = 80
    cell_side = 100
    line_thickness = 10
    maze = Maze(dimension1, dimension2)

    # Print the cell selected using the method defined in the task:
    print(maze.cell_at(dimension1 - 1, dimension2 - 1))

    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)
    img = Image.new("RGB", (width, height), (255, 255, 255))
    maze_img = ImageDraw.Draw(img)
    draw_grid(maze_img, maze.maze_grid.shape[0], maze.maze_grid.shape[1])

    # Highlight a selected cell using the method defined in the task:
    highlighted_cell = maze.cell_at(int(input('Enter x coordinate of cell to highlight: ')),
                                    int(input('Enter y coordinate of cell to highlight: ')))
    draw_cell(highlighted_cell, maze_img)
    img.save('highlighted_cell.png')
