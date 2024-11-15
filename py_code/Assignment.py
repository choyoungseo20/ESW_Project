import numpy as np

class Assignment:
    def __init__(self, width, height):
        self.appearance = 'retro'
        self.state = None
        self.position = np.array([width, height])