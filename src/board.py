from src.food import Food
from src.snake import Snake
from random import randrange
import numpy as np

class Board:

        
    def __init__(self, rows:int, columns:int):

        self.grid=np.full((columns, rows),"O",dtype=str)
        


