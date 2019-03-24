Aces Up Player
=====================================
This is a program I built after getting frustrated playing [Aces Up](https://en.wikipedia.org/wiki/Aces_Up). 

The game is notoriously luck-dependent and trying to win consisntely was pretty frustrating. Since the rules of play were relatively simple, I wrote this program to play 10,000 games at a time to determine the most viable strategies.

Different strategies for card movement when a space is available are implemented in the moveCards() method if you would like to add one. They are also described in further below.

How to Run
---------------
As of yet, the program is relatively simple, so you can just run it using `python playGame.py`.

If you do not already have `pydealer` installed, you will need to `pip install pydealer` first.

Strategies
---------------
These options are the strategies I have come up with so far when there is a chance to move a card. The most effective has been a combination of option 2 and option 3.

#### Option 1
Move the lowest card available.

#### Option 2
Move the highest card available.

#### Option 3
If the nth card and the n-1th card in any given column have the same suit, move the card from that column.

So far even the most effective strategy only wins ~1% of games (compared to only using option 1, which wins ~.38%).