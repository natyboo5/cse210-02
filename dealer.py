""" Hilo Game """

from card import Display_card

class Dealer:
    """A person who directs the game. 
    
    The dealer's responsability is to control the sequence of the game
    
    Attributes: 
        card(int): The value of the card drawn
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def _init_(self):
        """Constructor a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.is_playing = ''
        self.card = 0
        self.guess_card = 0
        self.guess = ''
        self.points = 0
        self.new_points = 0


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.points = 300
        self.is_playing = True

        while self.is_playing:
            print()
            display_card = Display_card()
            self.card = display_card.draw()
            print(f'The card is: {self.card}')

            self.get_input()
            self.output()
            self.update_points()
            self.play_again()

    def get_input(self): 
        
        self.guess = input('Higher or Lower [h/l]: ')

        display_card = Display_card()
        self.guess_card = display_card.draw()

        print(f'Next card was: {self.guess_card}')

        
    def update_points(self):
        
        self.points += self.new_points
        print(f'Your score is: {self.points}')
        
    
    def output(self):
        
        if (self.card < self.guess_card and self.guess == 'l') or (self.card > self.guess_card and self.guess == 'h'):
            self.new_points = -75
        else:
            self.new_points = 100
    
    
    def play_again(self):
        play = input('Play again [y/n]: ')

        if play == 'y':
            self.is_playing = True
        else:
            self.is_playing = False
