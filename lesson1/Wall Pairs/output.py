from task import Cell
from PIL import Image, ImageDraw

if __name__ == '__main__':
    cell = Cell(0, 0)
    print(f'The cell at {cell.x, cell.y} has all walls: {cell.has_all_walls()}')

    # Setting up dimensions and line coordinates:
    w, h = 200, 200
    line1, line2, line3, line4 = [(40, 40), (w - 40, 40)], \
                                 [(40, h - 40), (w - 40, h - 40)], \
                                 [(40, 40), (40, h - 40)], \
                                 [(w - 40, 40), (w - 40, h - 40)]

    lines = line1, line2, line3, line4
    filter_ = [x for x in cell.walls.values()]
    # Remove absent walls from `lines`:
    filtered_lines = [i for (i, v) in zip(lines, filter_) if v]

    # Creating new Image object:
    img = Image.new("RGB", (w, h), (255, 255, 255))

    # Create line image:
    img1 = ImageDraw.Draw(img)
    for line in filtered_lines:
        img1.line(line, fill="black", width=5)
    img.save("cell_walls.png")