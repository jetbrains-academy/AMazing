from cell import Cell
from PIL import Image, ImageDraw


def draw_cell(cell, image, color="black"):
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
        image.line(wall, fill=color, width=5)


def draw_grid(image, x_cells, y_cells):
    cells_ = generate_cells(x_cells, y_cells)
    for cell_ in cells_.values():
        draw_cell(cell_, image, "lightgray")


def draw_image(image, filename, *cells):
    img1 = ImageDraw.Draw(image)
    draw_grid(img1, get_dimensions(*cells)[0], get_dimensions(*cells)[1])
    for cell in cells:
        draw_cell(cell, img1)

    image.save(filename)


# The following two functions are needed for visualization here
# because we still don't have a Maze object, only the Cells.
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
    # dim1 = int(input())
    # dim2 = int(input())
    dim1, dim2 = 1, 2
    margin = 80
    cell_side = 100
    line_thickness = 10
    cells = generate_cells(dim1, dim2)
    width, height = (margin + cell_side * dim for dim in get_dimensions(*cells.values()))

    # Draw an image of two adjacent cells before knocking down the wall
    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw_image(img, "adjacent_cells.png", *cells.values())

    # Knock down an S wall of the (0,0) cell
    cells["Cell0"].knock_down_wall(cells["Cell1"], 'S')
    print(f'Cell 0 walls: {cells["Cell0"].walls}')
    print(f'Cell 1 walls: {cells["Cell1"].walls}')

    # Draw an image of two adjacent cells after knocking down the wall
    wall_img = Image.new("RGB", (width, height), (255, 255, 255))
    draw_image(wall_img, "removed_NS_wall.png", *cells.values())
