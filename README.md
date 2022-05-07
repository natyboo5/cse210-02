# cse210-02

How did you apply abstraction in your program’s design?

Hilo game consists of 2 parts. Part one, includes presenting a card to the player, and obtaining his input to start the game. The second part where, using the player's input, the game validates the input versus the next card obtained and therefore, it updates the current score. After this validation, the program will confirm if player has enough points to continue the game or not. If enough points remain, the player will have the chance to decide to continue the game. 

Considering these dynamics of the game, we are using abstraction by dividing the code into 2 classes as follows:

The first class has an object call Dealer.
     -	The responsibility of this class is to control the sequence of the play
     -    This class will contain the following functions (behaviors) and variables (states):
            
     BEHAVIORS:
     start_game (): Starts the game by running the main game loop.               
     get_input (): Ask the user to guess if the next card is higher or lower, and confirm the input is entered correctly (either "h" or "l" only). After      the input      is validated, call the function draw(self) and display a new card.
     output (): A method that determines the score for one round of play               
     update_points(self): A method that determines the score for the entire game               
     play_again (): Ask the user if he wants to play another round.
          
   STATES:
   card(int): The value of the card drawn
   is_playing (boolean): Whether or not the game is being played.
   guess_card(int): The value of card guessed
   guess(string): The guess input by the user (higher or lower)
   new_points (int): The score for one round of play.
   points (int): The score for the entire game.

The second class has an object call Display_card.
    -	The responsibility of this class is displaying the cards, one at a time whenever it is invoked. 
    -	This class contains one function and one state as follows:
    BEHAVIOR:
    drawn ():Draws a new card between 1 and 13, and return the number of the card.
    STATE
    card_number (int): chooses a number of card randomly.
    
    
    
    
README FILE

## Hilo Specification

Life is not a matter of holding good cards,
but sometimes, playing a poor hand well.

- Jack London -

## Overview

Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

## Rules

Hilo is played according to the following rules.

    The player starts the game with 300 points.
    Individual cards are represented as a number from 1 to 13.
    The current card is displayed.
    The player guesses if the next one will be higher or lower.
    The the next card is displayed.
    The player earns 100 points if they guessed correctly.
    The player loses 75 points if they guessed incorrectly.
    If a player reaches 0 points the game is over.
    If a player has more than 0 points they decide if they want to keep playing.
    If a player decides not to play again the game is over.

## Getting Started

You can run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure

---

The project files and folders are organized as follows:

```
root                    (project root folder)
  +-- card.py           (specific class)
  +-- dealer.py         (specific class)
  +-- __main__.py       (program entry point)
  +-- README.md         (general info)
```

## Required Technologies

---

- Python 3.8.0

## Authors

---

- Natalia Paredes
- Manuel Said Nava Ruiz
- Edgar Valderrama
- Diana Quispe

