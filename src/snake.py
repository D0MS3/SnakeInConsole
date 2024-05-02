import numpy as np
from src.pos import Pos


class SnakeElement:

    def __init__(self, startPosition, startDirection):
        self.actPosition:np.ndarray = np.array(startPosition)
        self.actDirection:np.ndarray = np.array(startDirection)

class Snake:
        
    def __init__(self, startPosition, startDirection):
        self.snakeElements =[]
        self.snakeElements.append(SnakeElement(startPosition,startDirection))

    def eat(self):

        evalPos = np.subtract(self.snakeElements[-1].actPosition,self.snakeElements[-1].actDirection)
        self.snakeElements.append(SnakeElement(evalPos,self.snakeElements[-1].actDirection))

    def move(self):
        # update positions
        for element in self.snakeElements:
            element.actPosition = np.add(element.actPosition,element.actDirection)
        # update directions for all elements except head
        for i in range(len(self.snakeElements)-1,0,-1):
            self.snakeElements[i].actDirection = np.copy(self.snakeElements[i-1].actDirection)

    def turnLeft(self):
        self.snakeElements[0].actDirection = np.matmul( self.snakeElements[0].actDirection,np.array([[0,1],[-1,0]]))

    def turnRight(self):
         self.snakeElements[0].actDirection = np.matmul( self.snakeElements[0].actDirection,np.array([[0,-1],[1,0]]))