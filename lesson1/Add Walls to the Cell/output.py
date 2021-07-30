from task import Cell
from PIL import Image, ImageDraw


if __name__ == '__main__':
    cell = Cell(0, 0)

    # Setting up dimensions and line coordinates:
    width, height = 200, 200
    line1, line2, line3, line4 = [(40, 40), (width - 40, 40)], \
                                 [(40, height - 40), (width - 40, height - 40)], \
                                 [(40, 40), (40, height - 40)], \
                                 [(width - 40, 40), (width - 40, height - 40)]

    lines = line1, line2, line3, line4
    shown_walls = [i for (i, v) in zip(lines, cell.walls.values()) if v]

    # Create new Image object:
    img = Image.new("RGB", (width, height), (255, 255, 255))

    # Create line image:
    walls_img = ImageDraw.Draw(img)
    for wall in shown_walls:
        walls_img.line(wall, fill="black", width=5)
    img.save("cell_walls.png")
