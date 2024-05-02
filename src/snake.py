import numpy as np

class SnakeElement:

    def __init__(self, startPosition, startDirection):
        self.actPosition:np.ndarray = np.array(startPosition)
        self.actDirection:np.ndarray = np.array(startDirection)

class Snake:
        
    def __init__(self, startPosition, startDirection):
        # define snake as list of single elements
        self.snakeElements =[]
        # create first snake element
        self.snakeElements.append(SnakeElement(startPosition,startDirection))

    def eat(self):
        evalPos = np.subtract(self.snakeElements[-1].actPosition,self.snakeElements[-1].actDirection)
        self.snakeElements.append(SnakeElement(evalPos,self.snakeElements[-1].actDirection))

    def starve(self):
        if len(self.snakeElements)>1:
            self.snakeElements.pop()

    def move(self):
        # update positions
        for element in self.snakeElements:
            element.actPosition = np.add(element.actPosition,element.actDirection)
        # update directions for all elements except head
        for i in range(len(self.snakeElements)-1,0,-1):
            self.snakeElements[i].actDirection = np.copy(self.snakeElements[i-1].actDirection)

    def turnLeft(self):
        rotMat = np.array([[0,1],[-1,0]])
        self.snakeElements[0].actDirection = np.matmul( self.snakeElements[0].actDirection, rotMat)

    def turnRight(self):
         rotMat = np.array([[0,-1],[1,0]])
         self.snakeElements[0].actDirection = np.matmul( self.snakeElements[0].actDirection, rotMat)