from PIL import Image, ImageDraw


class Cell:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}


if __name__ == '__main__':
    cell = Cell(0, 0)
    filter_ = [x for x in cell.walls.values()]

    # setting up dimensions and line coordinates
    w, h = 200, 200
    shape1, shape2, shape3, shape4 = [(40, 40), (w - 40, 40)], \
                                     [(40, 40), (40, h - 40)], \
                                     [(w - 40, 40), (w - 40, h - 40)], \
                                     [(40, h - 40), (w - 40, h - 40)]
    shapes = shape1, shape2, shape3, shape4
    filtered_shapes = [i for (i, v) in zip(shapes, filter_) if v]

    # creating new Image object
    img = Image.new("RGB", (w, h), (255, 255, 255))

    # create line image
    img1 = ImageDraw.Draw(img)
    for shape in filtered_shapes:
        img1.line(shape, fill="black", width=5)
    img.show()
    img.save("cell_walls.png")
