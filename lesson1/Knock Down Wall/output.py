from task import Cell
from PIL import Image, ImageDraw


def draw_cell(cell, image, color="black"):
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
        image.line(line, fill=color, width=5)


def draw_grid(image, x_cells, y_cells):
    cels = generate_cells(x_cells, y_cells)
    for cel in cels.values():
        draw_cell(cel, image, "lightgray")


def get_dimensions(*cells):
    return max([cell.x for cell in cells]) + 1, max([cell.y for cell in cells]) + 1


def draw_image(image, filename, *cells):
    img1 = ImageDraw.Draw(image)
    draw_grid(img1, get_dimensions(*cells)[0], get_dimensions(*cells)[1])
    for cell in cells:
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
    # dim1 = int(input())
    # dim2 = int(input())
    dim1, dim2 = 1, 2
    cells = generate_cells(dim1, dim2)

    w, h = (80 + 100 * dim for dim in get_dimensions(*cells.values()))

    # Draw an image of two adjacent cells before knocking down the wall
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw_image(img, "adjacent_cells.png", *cells.values())

    # Knock down an S wall of the (0,0) cell
    cells["Cell0"].knock_down_wall(cells["Cell1"], 'S')
    print(f'Cell 0 walls: {cells["Cell0"].walls}')
    print(f'Cell 1 walls: {cells["Cell1"].walls}')

    # Draw an image of two adjacent cells after knocking down the wall
    img2 = Image.new("RGB", (w, h), (255, 255, 255))
    draw_image(img2, "removed_NS_wall.png", *cells.values())
