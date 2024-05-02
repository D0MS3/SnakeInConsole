
import numpy as np

class Board:
        
    def __init__(self, rows:int, columns:int):

        self.grid=np.full((columns, rows),"O",dtype=str)
        


