class SQUARE:
    def __init__(self):
        self.side = 0
    def get_area(self):
        print(self.side*self.side)

square = SQUARE()
square.side = 32
square.get_area()
