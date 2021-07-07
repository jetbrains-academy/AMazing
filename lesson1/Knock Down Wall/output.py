from task import Cell
from PIL import Image, ImageDraw


def draw_cell(cell, image):
    filt = [x for x in cell.walls.values()]
    x = 90 if cell.x == 0 else 190
    y = 90 if cell.y == 0 else 190

    north, south, east, west = [(x - 50, y - 50), (x + 50, y - 50)], \
                               [(x - 50, y + 50), (x + 50, y + 50)], \
                               [(x + 50, y - 50), (x + 50, y + 50)], \
                               [(x - 50, y - 50), (x - 50, y + 50)]
    lines = north, south, east, west
    filtered_lines = [i for (i, v) in zip(lines, filt) if v]
    for line in filtered_lines:
        image.line(line, fill="black", width=5)


def draw_image(image, filename, *cells):
    img1 = ImageDraw.Draw(image)
    for cell in cells:
        draw_cell(cell, img1)

    image.show()
    image.save(filename)


if __name__ == '__main__':
    cell1 = Cell(0, 0)
    cell2 = Cell(1, 0)

    w, h = 280, 180

    # draw an image of two adjacent cells before knocking down the wall
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw_image(img, "adjacent_cells.png", cell1, cell2)

    # Knock down an E wall of the (0,0) cell
    cell1.knock_down_wall(cell2, 'E')
    print(f'Cell 1 walls: {cell1.walls}')
    print(f'Cell 2 walls: {cell2.walls}')

    # draw an image of two adjacent cells after knocking down the wall
    img2 = Image.new("RGB", (w, h), (255, 255, 255))
    draw_image(img2, "removed_E_wall.png", cell1, cell2)