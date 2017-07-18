def ticTacGame():
    #for the three rows and coloumns we have to assign number position on the board
    bp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
#winning chances for the game
    winningchances = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#this is to draw a board for the tic tack toe game where we can select each nuber to place the X and O instead of that number
    def drawboard():
        print(bp[0], bp[1], bp[2])
        print(bp[3], bp[4], bp[5])
        print(bp[6], bp[7], bp[8])
        print()
#player1 function where he select the number and replace the number place with the O
    def player11():
        n = select_num()
        if bp[n] == "X" or bp[n] == "O":
            print("\nYou can't go there. Try again")
            player11()
        else:
            bp[n] = "X"

# player2 function where he select the number and replace the number place with the X
#and also it should not selected the same as the player 1 choose the numbered position
    def player22():
        n = select_num()
        if bp[n] == "X" or bp[n] == "O":
            print("\nYou can't go there. Try again")
            player22()
        else:
            bp[n] = "O"
#selecting the number where we take the value valid number replace the numbers with the X and O
    def select_num():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nPLease try a number in the given board. Try again")
                        continue
                except ValueError:
                   print("\nPLease try a number in the given board. Try again")
                   continue
#now we have to write the logic where winning probabilities between the player one and two so we use the if and for loop
    def check_board():
        count = 0
        for a in winningchances:
            if bp[a[0]] == bp[a[1]] == bp[a[2]] == "X":
                print("Player 1 Wins!Congratulations! \n")
                return True

            if bp[a[0]] == bp[a[1]] == bp[a[2]] == "O":
                print("Player 2 Wins!Congratulations!\n")
                return True
        for a in range(9):
            if bp[a] == "X" or bp[a] == "O":
                count += 1
            if count == 9:
                print("The game ends as a Draw\n")
                return True
#in order to make turns one after the other we have to use this while logic so that player one plce first and after that player two will play.
    while not end:
        drawboard()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose to place a X")
        player11()
        print()
        drawboard()
        end = check_board()
        if end == True:
            break
        print("Player 2 choose to place a O")
        player22()
        print()
#in order to play the game again and again we have to call the function of tictactoe() game so it will restarts the game
    if input("Play again (y/n)\n") == "y":
        print()
        ticTacGame()

ticTacGame()