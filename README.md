# Tic-Tac-Toe

Welcome to my second project following the connect-4 project. This is a Tic-Tac-Toe game. The project goal is to design a tic-toe-game first using the console, and has a secondary goal of learning the tkinter library in python. The project will have a TODO list in this readme which is design to lead me to a first version of the project. Similar to my [connect-4](https://github.com/TheGreatDargon/Connect-4.git) project it will also feature some ideas I could do if I were to come back to the project.

# Design

To start the game will be a console based tic-tac-toe game allowing the player to change the size of the board, and the number of x's to win. The game will use X's and O's to define which player is which. After the game has been created through the console I/O I will start working with the [Tkinter](https://docs.python.org/3/library/tk.html) library to add a graphical element to the game.

To make moves there are a few ways we could make python input moves, the most straight forward way to have the user provide a tuple of the row/col they want to put their piece in. This tuple idea could also lead very nicely into the graphical side as well so it is at least a good candidate for how I want to design the method for placing pieces on the board. Another Idea which I think is cool is we could let the user choose between a number of rows and columns as an example below:

```
Choose a place to put your piece:
1. (0, 0)
2. (0, 1)
3. (0, 2)
```

As piece get placed those moves would be removed from the menu for example if the player chooses `(0, 0)` the menu would then look like:

```
Choose a place to put your piece:
1. (0, 1)
2. (0, 2)
```

I could see this getting unwieldy though and wouldn't fit for small console sizes, overall while I like what I could do with it, it seems like a poor choice.
<br>
The design I have fallen on is just to prompt the user for a (row, col) while this not a extremely user friendly way of working through the input issue, I think that it is overall better to work on it this way as this isn't the intended way for a user to enter moves when the project is finished. Here is a mock up of what the game could look like:

```
      1     2     3
   -------------------
1  |  O  |  X  |     |
   -------------------
2  |     |  X  |  O  |
   -------------------
3  |     |     |     |
   -------------------

please enter your move (row, col):
```

A final note, in my connect-4 project I used two different methods for one versus two player, and thus two different methods for a gameplay loop, I want to have this just be one method for the gameplay loop which just uses a default value to decide which to choose.

# TODO

- [X] Create main method menu with options for one player, two player, change dimensions and quit
- [ ] Create the board using a data structure (maybe something better than 2d nparray?)
- [X] Create helper method for the gameplay loop
- [X] Create helper method for player to place a piece on the board
- [ ] Create helper method for changing the dimensions of the board