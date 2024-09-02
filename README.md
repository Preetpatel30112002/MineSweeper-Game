_**Minesweeper Game:**_

This is a Python implementation of the classic Minesweeper game, where players attempt to clear a grid of hidden mines without detonating any. The game is played on a 10x10 board, with a random distribution of 10 bombs. The player can either "dig" to uncover a cell or "flag" a cell that they suspect contains a bomb. The game ends when all non-bomb cells are uncovered, or when the player digs a bomb.

_**How to Play**_
  
  1)Board Setup:
  
    -The game board consists of a 10x10 grid, where each cell is either empty, contains a bomb (*), or displays a number representing the count of bombs in adjacent cells.
    -The player’s goal is to uncover all cells without triggering a bomb.
    
  2)User Actions:
  
    -The player inputs coordinates to either dig or flag a cell.
    
    -To dig a cell, enter the coordinates in the format row,column (e.g., 1,1).
    
    -To flag a cell (suspected of containing a bomb), add an f after the coordinates (e.g., 1,1f).
    
  3)Game Rules:
  
    -If a cell with a bomb is dug, the game is over.
    -If a cell with no surrounding bombs (0) is dug, all neighboring cells are automatically uncovered.
    -The game is won when all non-bomb cells are uncovered.
    
  4)Game End:
    -The game ends when the player hits a bomb or successfully uncovers all safe cells.
    -After the game ends, the player has the option to replay.

_**License:**_

  -This Minesweeper game is open-source and free to use under the MIT License.
