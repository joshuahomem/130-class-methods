#!python3
"""
Tic Tac Toe
Create a tic tac toe game that is enclosed entirely within a function.  The basic shell has been created, as well as the main block that will be used to execute the class method that runs the game.
You need to create the methods and class variables that you will use.

One idea would be to create a board like so:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

or you could also use the keypad to help choose positions:

7 | 8 | 9
---------
4 | 5 | 6
---------
1 | 2 | 3

To enhance your display, you can access unicode symbols
╩ for example: https://altcodeunicode.com/
"""

class tictactoe:
    lines = ['7','8','9',
             '4','5','6',
             '1','2','3']
    turn = 1
    game_over = False
    winning = [[1,1,1,0,0,0,0,0,0],
               [0,0,0,1,1,1,0,0,0], 
               [0,0,0,0,0,0,1,1,1],
               [1,0,0,1,0,0,1,0,0],
               [0,1,0,0,1,0,0,1,0],
               [0,0,1,0,0,1,0,0,1],
               [1,0,0,0,1,0,0,0,1],
               [0,0,1,0,1,0,1,0,0]]

    @classmethod
    def run(cls):
        while cls.game_over == False:
            cls.printBoard()
            a = str(input("Where Would you liek to place you first move: "))
            cls.move(a)
            cls.check_game_over()

    @classmethod
    def printBoard(cls):
        print(cls.lines[0] + " | " + cls.lines[1] + " | " + cls.lines[2])
        print('--+---+--')
        print(cls.lines[3] + " | " + cls.lines[4] + " | " + cls.lines[5])
        print('--+---+--')
        print(cls.lines[6] + " | " + cls.lines[7] + " | " + cls.lines[8])
        print("")

    @classmethod
    def move(cls, a):
        if cls.turn % 2 == 0:
            symbol = "X"
        else:
            symbol = "O"
        if a not in cls.lines:
            print("Invalid spot.")
        else:
            for i in range(len(cls.lines)):
                if cls.lines[i] == a:
                    cls.lines[i] = symbol
                    cls.turn += 1

    @classmethod
    def check_game_over(cls):
        Ocombo = []
        Xcombo = []

        if cls.turn <= 9:
            for i in range(len(cls.lines)):
                if cls.lines[i] == "O":
                    Ocombo.append(1)
                else:
                    Ocombo.append(0)

            for i in range(len(cls.lines)):
                if cls.lines[i] == "X":
                    Xcombo.append(1)
                else:
                    Xcombo.append(0)
                    
            for combination in cls.winning:
                if combination == Ocombo:
                    print("O's Have won")
                    cls.game_over = True

                elif combination == Xcombo:
                    print("X's have won")
                    cls.game_over = True
                
                else:
                    cls.game_over = False
        else:
            print("Tie Game")
            cls.game_over = True


tictactoe.run()
