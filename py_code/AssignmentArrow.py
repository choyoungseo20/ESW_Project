import numpy as np
import math

class AssignmentArrow:
    def __init__(self, start_position, target_position):
        self.appearance = 'retro'
        self.state = None
        self.speed = 5
        self.position = np.array([start_position[0], start_position[1]])
        self.direction = np.array([target_position[0] - start_position[0], target_position[1] - start_position[1]])
        self.magnitude = math.sqrt(self.direction[0]**2 + self.direction[1]**2)
        self.velocity = np.array([(self.direction[0] / self.magnitude) * self.speed, (self.direction[1] / self.magnitude) * self.speed])

        
    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    