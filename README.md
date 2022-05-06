# cse210-02

How did you apply abstraction in your program’s design?

In python when we talk about abstraction, we are talking about classes, in the design of our Hilo program we created 2 classes.

The first class has an object call Dealer.
     •	The responsibility of this class is to control the sequence of the play.

The second class has an object call Card.
    •	The responsibility of this class is displaying the cards, one at a time. 
    •	There is one behavior or function “drawn ()” that will use one variable “card_number”, this function will generate the random number of the card. 
    
    
    
    
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

