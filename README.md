Minesweeper Game
This is a Python implementation of the classic Minesweeper game, where players attempt to clear a grid of hidden mines without detonating any. The game is played on a 10x10 board, with a random distribution of 10 bombs. The player can either "dig" to uncover a cell or "flag" a cell that they suspect contains a bomb. The game ends when all non-bomb cells are uncovered, or when the player digs a bomb.

How to Play
Board Setup:

The game board consists of a 10x10 grid, where each cell is either empty, contains a bomb (*), or displays a number representing the count of bombs in adjacent cells.
The player’s goal is to uncover all cells without triggering a bomb.
User Actions:

The player inputs coordinates to either dig or flag a cell.
To dig a cell, enter the coordinates in the format row,column (e.g., 1,1).
To flag a cell (suspected of containing a bomb), add an f after the coordinates (e.g., 1,1f).
Game Rules:

If a cell with a bomb is dug, the game is over.
If a cell with no surrounding bombs (0) is dug, all neighboring cells are automatically uncovered.
The game is won when all non-bomb cells are uncovered.
Game End:

The game ends when the player hits a bomb or successfully uncovers all safe cells.
After the game ends, the player has the option to replay.

Getting Started
Prerequisites
Python 3.x installed on your system.
Running the Game
Save the code in a file named minesweeper.py.

Run the script using the Python interpreter:

bash
Copy code
python minesweeper.py
Follow the on-screen instructions to play.

Future Enhancements
Add different difficulty levels with varying board sizes and bomb counts.
Implement a graphical user interface (GUI) for a more interactive experience.
Allow saving and loading game states.
License
This Minesweeper game is open-source and free to use under the MIT License.
