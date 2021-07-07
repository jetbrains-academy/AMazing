from task import Cell
from PIL import Image, ImageDraw


if __name__ == '__main__':
    cell = Cell(0, 0)
    filter_ = [x for x in cell.walls.values()]

    # setting up dimensions and line coordinates
    w, h = 200, 200
    line1, line2, line3, line4 = [(40, 40), (w - 40, 40)], \
                                 [(40, h - 40), (w - 40, h - 40)], \
                                 [(40, 40), (40, h - 40)], \
                                 [(w - 40, 40), (w - 40, h - 40)]

    lines = line1, line2, line3, line4
    filtered_lines = [i for (i, v) in zip(lines, filter_) if v]

    # creating new Image object
    img = Image.new("RGB", (w, h), (255, 255, 255))

    # create line image
    img1 = ImageDraw.Draw(img)
    for line in filtered_lines:
        img1.line(line, fill="black", width=5)
    img.show()
    img.save("cell_walls.png")