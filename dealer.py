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
            self.card = display_card.drawn()
            print(f'The card is: {self.card}')

            self.get_input()
            self.output()
            self.update_points()
            
            if self.is_playing == False:
                break
                
            self.play_again()

    def get_input(self): 
        """Ask the user to guess if the next card is higher or lower, and confirm the input is entered correctly (either "h" or "l" only).
        After the input is validated, call the function draw(self) and display a new card.

        Args:
            self (Dealer): an instance of Dealer.
        """
        
        while True:
            self.guess = input('Higher or Lower [h/l]: ').lower()

            if self.guess == 'l' or self.guess == 'h':

                while True:
                    display_card = Display_card()
                    self.guess_card = display_card.drawn()
                    if self.guess_card == self.card:
                        continue
                    else:
                        break

                print(f'Next card was: {self.guess_card}')
                break
                
            else:
                print('Wrong letter')
                continue

        
    def update_points(self):
        """A method that determines the score for the entire game
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        
        self.points += self.new_points
        if self.points <= 0:
            self.is_playing = False
            print('You do not have enough points')
        else:
            print(f'Your score is: {self.points}')
        
    
    def output(self):
    
        """A method that determines the score for one round of play
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        
        if (self.card < self.guess_card and self.guess == 'l') or (self.card > self.guess_card and self.guess == 'h'):
            self.new_points = -75
        else:
            self.new_points = 100
    
    
    def play_again(self):
        """Ask the user if he wants to play another round.
        
        Args:
            self (Dealer): an instance of Dealer.
        """

        play = input('Play again [y/n]: ')

        if play == 'y':
            self.is_playing = True
        else:
            self.is_playing = False
