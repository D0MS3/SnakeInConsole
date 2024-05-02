import time
from src.board import Board
from src.game import Game

myGame = Game()

while(1):
    
    inp = input('Command: ')
    if inp == 'r':
        myGame.mySnake.turnRight()
    elif inp == 'l':
        myGame.mySnake.turnLeft()
    elif inp == 'e':
        myGame.mySnake.eat()
    elif inp == 'm':
        myGame.mySnake.move()
    else:
        pass  

    myGame.update()
    myGame.renderBoard()
  
