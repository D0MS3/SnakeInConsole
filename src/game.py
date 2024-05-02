from src.food import Food
from src.snake import Snake
from src.board import Board
from random import randrange
import numpy as np

BOARD_WIDTH=10
BOARD_HEIGHT=10
SNAKE_START_POS=[5,5]
SNAKE_START_DIR=[1,0]
NUM_FOOD=3

class Game:
    def __init__(self):
        self.myBoard=Board(BOARD_WIDTH,BOARD_HEIGHT)
        self.mySnake=Snake(SNAKE_START_POS,SNAKE_START_DIR)
        self.myFoods=self.createRndFoods(NUM_FOOD)

    def createRndFoods(self,numFood:int):
        foods=[]
        for i in range(numFood):
            foods.append(Food([randrange(0,BOARD_HEIGHT),randrange(0, BOARD_WIDTH)]))
        return foods


    def checkForBoundaries(self) -> bool:
        for ele in self.mySnake.snakeElements:
            if(ele.actPosition[0]>=BOARD_WIDTH 
               or ele.actPosition[1]>=BOARD_HEIGHT
               or ele.actPosition[0]<0 
               or ele.actPosition[1]<0):
                print("out of bounce --> LOST!")
                exit()

    def checkBoundaries2(s: Snake, b: Board) -> bool:
        # checks if snake is within Board boundaries
        # TODO
        pass

    def checkForFood(self):
        for food in self.myFoods:
            if(np.array_equal(food.actPosition,self.mySnake.snakeElements[0].actPosition)):
                self.myFoods.remove(food)
                self.mySnake.eat()
        if(not self.myFoods):
                self.myFoods.extend(self.createRndFoods(NUM_FOOD))

    def checkForSelfCollision(self):
        for ele in self.mySnake.snakeElements[1:]:
            if np.array_equal(ele.actPosition,self.mySnake.snakeElements[0].actPosition):
                print("self collision --> LOST!")
                exit()
    
    def update(self): 
        self.checkForFood()
        self.checkForBoundaries()
        self.checkForSelfCollision()
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