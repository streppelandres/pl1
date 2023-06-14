class Card:
    number: int
    color: tuple
    flipped: bool
    rect_collision: any

    def __init__(self, number: int, color: tuple):
        self.number = number
        self.color = color
        self.flipped = False

    def __str__(self):
        return ''.join([
            f'Number: {self.number} ',
            f'Color: {self.color} ',
            f'Flipped: {self.flipped}'
        ])
