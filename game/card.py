import random


class DisplayCard:
    """Generates a random card between 1 to 13
    """

    def __init__(self):
        self.card_number = 0

    def drawn(self):
        """Draws a new card between 1 and 13, and return the number of the card.

        """
        self.card_number = random.randint(1, 13)
        return self.card_number

    def card_text(self):
        method = 'c_' + str(self.card_number)
        return getattr(self, method)()

    def c_1(self):
        return """
             _____
            |A ^  |
            | / \ |
            | \ / |
            |  .  |
            |____V|
        """

    def c_2(self):
        return """
            _____
           |2    |
           |  ^  |
           |     |
           |  ^  |
           |____Z|
        """

    def c_3(self):
        return """
             _____
            |3    |
            | ^ ^ |
            |     |
            |  ^  |
            |____E|
        """

    def c_4(self):
        return """
             _____
            |4    |
            | ^ ^ |
            |     |
            | ^ ^ |
            |____h|
        """

    def c_5(self):
        return """
             _____
            |5    |
            | ^ ^ |
            |  ^  |
            | ^ ^ |
            |____S|
        """

    def c_6(self):
        return """
             _____
            |6    |
            | ^ ^ |
            | ^ ^ |
            | ^ ^ |
            |____9|
        """

    def c_7(self):
        return """
             _____
            |7    |
            | ^ ^ |
            |^ ^ ^|
            | ^ ^ |
            |____L|
        """

    def c_8(self):
        return """
             _____
            |8    |
            |^ ^ ^|
            | ^ ^ |
            |^ ^ ^|
            |____8|
        """

    def c_9(self):
        return """
             _____
            |9    |
            |^ ^ ^|
            |^ ^ ^|
            |^ ^ ^|
            |____9|
        """

    def c_10(self):
        return """
             _____
            |10 ^ |
            |^ ^ ^|
            |^ ^ ^|
            |^ ^ ^|
            |___0I|
        """

    def c_11(self):
        return """
             _____
            |J  ww|
            | ^ {)|
            |(.)% |
            | | % |
            |__%%[|
        """

    def c_12(self):
        return """
             _____
            |Q  ww|
            | ^ {(|
            |(.)%%|
            | |%%%|
            |_%%%O|
        """

    def c_13(self):
        return """
             _____
            |K  WW|
            | ^ {)|
            |(.)%%|
            | |%%%|
            |_%%%>|
        """
