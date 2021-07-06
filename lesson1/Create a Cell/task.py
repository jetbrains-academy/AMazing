class Cell:

    def __init__(self, x, y):
        self.x, self.y = x, y


if __name__ == '__main__':
    cell = Cell(0, 0)
    print(f'Cell\n'
          f'coordinate x: {cell.x}\n'
          f'coordinate y: {cell.y}')
