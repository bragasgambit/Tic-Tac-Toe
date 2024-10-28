# Tic Tac Toe
#### [YouTube Video](https://www.youtube.com/watch?v=ZRzwWXZbcXY)
#### Description:
Project Title: This is Tic-Tac-Toe <br>
Name: Yuri R Braga <br>
GitHub Username: [bragasgambit](https://github.com/bragasgambit) <br>
edX Username: [YuriRBraga](https://profile.edx.org/u/YuriRBraga) <br>
City/Country: Campinas, Brazil <br>
Date: October, 28th, 2024

Tic-Tac-Toe, also known as Noughts and Crosses or X's and O's, is a simple yet strategic game played on a 3x3 grid.
The game is widely popular due to its simplicity, ease of play, and the minimal materials required – just a piece of paper and a pen or pencil.
Despite its straightforward nature, Tic-Tac-Toe presents basic strategic thinking concepts, making it a valuable tool for introducing young players to logical reasoning, game theory, and the basics of artificial intelligence (minimax algorithm).

A Tic-Tac-Toe game for 2 players where one can fight each other in 255168 possible games to win, draw or loose if you not smart enought to predict next moves.
The game is fully operational with checkers where Player 1 wins, Player 2 or a Draw. The code is divided into helpers.py and main.py.
helpers.py contain init_board(), check_turn(), check_win() functions that are crucial for the program's well functioning when playing PvP.
helpers.py also include minimax() and find_best_move() for PvE games, where you will not win, since the algorithm will find always the best positioning based on win = 1, draw = 0, and lose = -1. The engine will always calculate the >= 0 value for player 2 (AI) based on all games possible.

main.py is where the "frontend" part of the game is (mechanics -"backend"- are located on helpers.py). To create the board, I made a dictionary with the key spot pointing to its value, so it can be changed when the game progress'. The code os.system("cls") for Windows was used to clear the terminal for no polution at the terminal, simulating a paper that is scratched over and over for the next steps, like a real Tic-Tac-Toe game.
The clean code that was made offers two options of a game where the player can choose: PvP or PvE. PvP is a chance for you to win against your friends. PvE you will never win, as explained above.

I choose the Tic-Tac_Toe for the moderate difficulty in implement AI and the spark in the AI Lecture where David Malan talks about the first babysteps to build a Minority Report or Terminator in real life (he did not say that, but my brain went that way... maybe a degree of cyberpsychosis). Well, enjoy the start of the end :)

This was Tic-Tac-Toe
