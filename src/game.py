from src.food import Food
from src.snake import Snake
from src.board import Board
from random import randrange
import numpy as np

BOARD_WIDTH=10
BOARD_HEIGHT=10
SNAKE_START_POS=[5,5]
SNAKE_START_DIR=[1,0]
NUM_FOOD=15

class Game:
    def __init__(self):
        self.myBoard=Board(BOARD_WIDTH,BOARD_HEIGHT)
        self.mySnake=Snake(SNAKE_START_POS,SNAKE_START_DIR)
        self.myFoods=self.createFoods(NUM_FOOD)

    def createFoods(self,numFood:int):
        foods=[]
        for i in range(numFood):
            foods.append(Food([randrange(0,BOARD_HEIGHT),randrange(0, BOARD_WIDTH)]))
        return foods
    
    def createRndFood(self):
        self.food=Food([randrange(0,BOARD_HEIGHT),randrange(0, BOARD_WIDTH)])
    
    def update(self):    
        for f in self.myFoods:
            if(np.array_equal(f.actPosition,self.mySnake.snakeElements[0].actPosition)):
               # delete food
               self.myFoods.remove(f)
               # increase snake length
               self.mySnake.eat()
    
               
      
        # boundaries checken???
        # move snake auswerten

    def clearBoard(self):
        lineUp = '\033[A'
        lineClear='\x1b[2K'
        for idx in range(11):
            print(lineUp, end=lineClear)

    def renderBoard(self):
        self.clearBoard()
        self.myBoard.grid.fill('O')
        #insert food
        for food in self.myFoods:
            self.myBoard.grid[food.actPosition[0],food.actPosition[1]]='F'

         # insert snake
        for snakeEle in self.mySnake.snakeElements:
            self.myBoard.grid[snakeEle.actPosition[0],snakeEle.actPosition[1]]="S"
       
        # print board status
        for i in range(self.myBoard.grid.shape[0]):
            for j in range(self.myBoard.grid.shape[1]):
                print(self.myBoard.grid[i][j], end="")
            print()