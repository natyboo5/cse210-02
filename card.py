import random


class Display_card:
    """Generates a random card between 1 to 13

    """

    def __init__(self):
        self.card_number = 0

    def draw(self):
        self.card_number = random.randint(1, 13)
        return self.card_number
